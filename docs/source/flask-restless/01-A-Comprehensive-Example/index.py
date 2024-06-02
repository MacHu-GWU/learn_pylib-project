# -*- coding: utf-8 -*-

"""
这是一个我自己写的用 flask-restless 构建一个简单的 API 的例子.

由于 flask-restless 的核心使用场景就是让用户专注于定义 Data Model 和 Relationship,
然后由 flask-restless 来生成 API server, 并且一定不仅要支持单个 Data Model 的增删查改,
还要支持对 relationship 的增删查改.

所以在这个例子中, 我用 youtube 作为例子, 模拟了用户, 视频, 播放列表, 视频和播放列表之间的关系.
这个例子包含了 one-to-many 和 many-to-many 的关系. 无论你的模型有多复杂, 只要符合标准范式,
那么都可以用这个例子中的方法来定义 Data Model 和 Relationship.
"""

import typing as T
import json
import uuid
import requests
from datetime import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm

from rich import print as rprint
from rich.console import Console
from rich.panel import Panel

from app import path_db, User, Video, Playlist, playlist_video, ETE

engine = sa.create_engine(f"sqlite:///{path_db}")

host = "http://127.0.0.1:5000"
post_headers = {
    "Content-Type": "application/vnd.api+json",
    "Accept": "application/vnd.api+json",
}
get_headers = {
    "Accept": "application/vnd.api+json",
}
console = Console()


def get_utc_now():
    return datetime.utcnow()


def clear_data():
    with engine.connect() as conn:
        conn.execute(Video.__table__.delete())
        conn.execute(User.__table__.delete())
        conn.execute(Playlist.__table__.delete())
        conn.execute(playlist_video.delete())
        conn.commit()


def make_request(meth: T.Callable, kwargs: T.Dict[str, T.Any]) -> requests.Response:
    """
    A helper function that make HTTP request, and automatically print request and response.
    """
    console.rule("API Request")
    rprint(kwargs)

    response: requests.Response = meth(**kwargs)
    console.rule("API Response status code")
    rprint(f"{response.status_code = }")
    console.rule("API Response headers")
    rprint(dict(response.headers))
    console.rule("API Response data")
    if response.status_code in [200, 201]:
        rprint(json.loads(response.text))
    elif response.status_code == 204:
        print("No content")
    else:
        rprint(response.text)
    return response


clear_data()

# ------------------------------------------------------------------------------
# Create a user
# ------------------------------------------------------------------------------
rprint(Panel("Create a user"))
user_id_1 = str(uuid.uuid4())
user_id_1_create_at = get_utc_now()

url = f"{host}/api/{ETE.user.value}"
data = {
    "data": {
        "type": ETE.user.value,
        "id": user_id_1,
        "attributes": {
            "name": "Alice",
            "create_at": user_id_1_create_at.isoformat(),
            "update_at": user_id_1_create_at.isoformat(),
            "deleted": 0,
        },
    },
}
kwargs = dict(
    url=url,
    headers=post_headers,
    json=data,
)
response = make_request(requests.post, kwargs)

# verify the data in the database
with orm.Session(engine) as ses:
    user = ses.get(User, user_id_1)
    assert user.id == user_id_1
    assert user.name == "Alice"
    assert user.create_at == user_id_1_create_at
    assert user.update_at == user_id_1_create_at
    assert user.deleted == 0


# ------------------------------------------------------------------------------
# Get user 1
# ------------------------------------------------------------------------------
rprint(Panel("Get user 1"))
url = f"{host}/api/{ETE.user.value}/{user_id_1}"
kwargs = dict(
    url=url,
    headers=get_headers,
)
response = make_request(requests.get, kwargs)
data = json.loads(response.text)
assert data["data"]["id"] == user_id_1
assert data["data"]["attributes"]["name"] == "Alice"
assert data["data"]["attributes"]["deleted"] == 0
assert data["data"]["attributes"]["create_at"] == user_id_1_create_at.isoformat()
assert data["data"]["attributes"]["update_at"] == user_id_1_create_at.isoformat()

# ------------------------------------------------------------------------------
# Update the user 1
# ------------------------------------------------------------------------------
rprint(Panel("Update the user 1"))
url = f"{host}/api/{ETE.user.value}/{user_id_1}"

user_id_1_update_at = get_utc_now()
data = {
    "data": {
        "type": ETE.user.value,
        "id": user_id_1,
        "attributes": {
            "name": "Bob",
            "update_at": user_id_1_update_at.isoformat(),
        },
    },
}
kwargs = dict(
    url=url,
    headers=post_headers,
    json=data,
)
response = make_request(requests.patch, kwargs)

# verify the data in the database
with orm.Session(engine) as ses:
    user = ses.get(User, user_id_1)
    assert user.id == user_id_1
    assert user.name == "Bob"
    assert user.create_at == user_id_1_create_at
    assert user.update_at == user_id_1_update_at
    assert user.deleted == 0

# ------------------------------------------------------------------------------
# Create a video
# ------------------------------------------------------------------------------
rprint(Panel("Create a video"))
video_id_1 = str(uuid.uuid4())
video_id_1_create_at = get_utc_now()

url = f"{host}/api/{ETE.video.value}"
data = {
    "data": {
        "type": ETE.video.value,
        "id": video_id_1,
        "attributes": {
            "title": "user 1 video 1",
            "create_at": video_id_1_create_at.isoformat(),
            "update_at": video_id_1_create_at.isoformat(),
            "deleted": 0,
            "author_id": user_id_1,
        },
    },
}
kwargs = dict(
    url=url,
    headers=post_headers,
    json=data,
)
response = make_request(requests.post, kwargs)

# verify the data in the database
with orm.Session(engine) as ses:
    video = ses.get(Video, video_id_1)
    assert video.id == video_id_1
    assert video.title == "user 1 video 1"
    assert video.create_at == video_id_1_create_at
    assert video.update_at == video_id_1_create_at
    assert video.deleted == 0
    assert video.author_id == user_id_1
    assert video.author.id == user_id_1
    assert video.author.name == "Bob"

    user = ses.get(User, user_id_1)
    owned_videos = user.owned_videos
    assert len(owned_videos) == 1
    video = owned_videos[0]
    assert video.id == video_id_1
    assert video.title == "user 1 video 1"
    assert video.create_at == video_id_1_create_at
    assert video.update_at == video_id_1_create_at
    assert video.deleted == 0

# ------------------------------------------------------------------------------
# Update video ownership relationship
# ------------------------------------------------------------------------------
rprint(Panel("Update video ownership relationship"))
# create a new user, so we can switch the ownership to this new user
user_id_2 = str(uuid.uuid4())
user_id_2_create_at = get_utc_now()

url = f"{host}/api/{ETE.user.value}"
data = {
    "data": {
        "type": ETE.user.value,
        "id": user_id_2,
        "attributes": {
            "name": "Bella",
            "create_at": user_id_2_create_at.isoformat(),
            "update_at": user_id_2_create_at.isoformat(),
            "deleted": 0,
        },
    },
}
kwargs = dict(
    url=url,
    headers=post_headers,
    json=data,
)
requests.post(**kwargs)

# update video ownership
url = f"{host}/api/{ETE.video.value}/{video_id_1}/relationships/author"
data = {
    "data": {
        "type": ETE.user.value,
        "id": user_id_2,
    },
}
kwargs = dict(
    url=url,
    headers=post_headers,
    json=data,
)
response = make_request(requests.patch, kwargs)

# verify the data in the database
with orm.Session(engine) as ses:
    video = ses.get(Video, video_id_1)
    assert video.author_id == user_id_2

# ------------------------------------------------------------------------------
# Create playlist video relationship
# ------------------------------------------------------------------------------
rprint(Panel("Create playlist video relationship"))
# first, create two more videos and two playlists
# now we have 3 videos and 2 playlists
video_id_2 = str(uuid.uuid4())
video_id_3 = str(uuid.uuid4())
playlist_id_1 = str(uuid.uuid4())
playlist_id_2 = str(uuid.uuid4())
utc_now = get_utc_now()

url = f"{host}/api/{ETE.video.value}"
for ith, video_id in enumerate([video_id_2, video_id_3], start=2):
    data = {
        "data": {
            "type": ETE.video.value,
            "id": video_id,
            "attributes": {
                "title": f"user 1 video {ith}",
                "create_at": utc_now.isoformat(),
                "update_at": utc_now.isoformat(),
                "deleted": 0,
                "author_id": user_id_1,
            },
        },
    }
    kwargs = dict(
        url=url,
        headers=post_headers,
        json=data,
    )
    requests.post(**kwargs)

url = f"{host}/api/{ETE.playlist.value}"
for ith, playlist_id in enumerate([playlist_id_1, playlist_id_2], start=1):
    data = {
        "data": {
            "type": ETE.playlist.value,
            "id": playlist_id,
            "attributes": {
                "title": f"user 1 playlist {ith}",
                "create_at": utc_now.isoformat(),
                "update_at": utc_now.isoformat(),
                "deleted": 0,
                "owner_id": user_id_1,
            },
        },
    }
    kwargs = dict(
        url=url,
        headers=post_headers,
        json=data,
    )
    requests.post(**kwargs)

# playlist 1 includes video 1 and video 2
# playlist 2 includes video 2 and video 3
url = f"{host}/api/{ETE.playlist.value}/{playlist_id_1}/relationships/videos"
data = {
    "data": [
        {
            "type": ETE.video.value,
            "id": video_id_1,
        },
        {
            "type": ETE.video.value,
            "id": video_id_2,
        },
    ],
}
kwargs = dict(
    url=url,
    headers=post_headers,
    json=data,
)
response = make_request(requests.patch, kwargs)

url = f"{host}/api/{ETE.playlist.value}/{playlist_id_2}/relationships/videos"
data = {
    "data": [
        {
            "type": ETE.video.value,
            "id": video_id_2,
        },
        {
            "type": ETE.video.value,
            "id": video_id_3,
        },
    ],
}
kwargs = dict(
    url=url,
    headers=post_headers,
    json=data,
)
response = make_request(requests.patch, kwargs)

# verify the data in the database
with orm.Session(engine) as ses:
    playlist = ses.get(Playlist, playlist_id_1)
    assert {video.id for video in playlist.videos} == {
        video_id_1,
        video_id_2,
    }
    video = ses.get(Video, video_id_2)
    assert {playlist.id for playlist in video.playlists} == {
        playlist_id_1,
        playlist_id_2,
    }

# ------------------------------------------------------------------------------
# Update playlist video relationship
# ------------------------------------------------------------------------------
rprint(Panel("Update playlist video relationship"))

url = f"{host}/api/{ETE.playlist.value}/{playlist_id_1}/relationships/videos"
data = {
    "data": [
        {
            "type": ETE.video.value,
            "id": video_id_1,
        },
        {
            "type": ETE.video.value,
            "id": video_id_3,
        },
    ],
}
kwargs = dict(
    url=url,
    headers=post_headers,
    json=data,
)
response = make_request(requests.patch, kwargs)

# verify the data in the database
with orm.Session(engine) as ses:
    playlist = ses.get(Playlist, playlist_id_1)
    assert {video.id for video in playlist.videos} == {
        video_id_1,
        video_id_3,
    }
