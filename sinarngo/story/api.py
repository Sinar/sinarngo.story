from plone.jsonapi.routes import add_plone_route

# CRUD
from plone.jsonapi.routes.api import get_items
from plone.jsonapi.routes.api import create_items
from plone.jsonapi.routes.api import update_items
from plone.jsonapi.routes.api import delete_items

from plone.jsonapi.routes.api import url_for


# GET
@add_plone_route("/story", "story", methods=["GET"])
@add_plone_route("/story/<string:uid>", "story", methods=["GET"])
def get(context, request, uid=None):
    """ get story
    """
    items = get_items("sinarngo.story.story", request, uid=uid, endpoint="story")
    return {
        "url": url_for("story"),
        "count": len(items),
        "items": items,
    }


# CREATE
@add_plone_route("/story/create", "story_create", methods=["POST"])
@add_plone_route("/story/create/<string:uid>", "story_create", methods=["POST"])
def create(context, request, uid=None):
    """ create story
    """
    items = create_items("sinarngo.story.story", request, uid=uid, endpoint="story")
    return {
        "url": url_for("story_create"),
        "count": len(items),
        "items": items,
    }


# UPDATE
@add_plone_route("/story/update", "story_update", methods=["POST"])
@add_plone_route("/story/update/<string:uid>", "story_update", methods=["POST"])
def update(context, request, uid=None):
    """ update story
    """
    items = update_items("sinarngo.story.story", request, uid=uid, endpoint="story")
    return {
        "url": url_for("story_update"),
        "count": len(items),
        "items": items,
    }


# DELETE
@add_plone_route("/story/delete", "story_delete", methods=["POST"])
@add_plone_route("/story/delete/<string:uid>", "story_delete", methods=["POST"])
def delete(context, request, uid=None):
    """ delete story
    """
    items = delete_items("sinarngo.story.story", request, uid=uid, endpoint="story")
    return {
        "url": url_for("story_delete"),
        "count": len(items),
        "items": items,
    }


