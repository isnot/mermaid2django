from django.contrib import admin

from .models import (
    Character,
    Comic,
    Fragment,
    Journey,
    Magazine,
    Person,
    Photo,
    Place,
    Route,
    Scene,
    Series,
    Step,
    Story,
    Tweet,
    Type_master,
    User,
    Venue,
    Web_comic,
)


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    fields = ["author", "label", "magazine_title", "publisher", "rel_series_id", "short_title", "site", "title"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "author", "label", "magazine_title", "publisher", "rel_series_id", "short_title", "site", "title",)
    list_display_links = ("author", "label", "magazine_title", "publisher", "rel_series_id", "short_title", "site", "title",)


@admin.register(Comic)
class ComicAdmin(admin.ModelAdmin):
    fields = ["cover_image_url", "isbn", "issued", "memo", "number", "obi", "released", "title", "series"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "cover_image_url", "isbn", "issued", "memo", "number", "obi", "released", "title", "series",)
    list_display_links = ("cover_image_url", "isbn", "issued", "memo", "number", "obi", "released", "title", "series",)


@admin.register(Web_comic)
class Web_comicAdmin(admin.ModelAdmin):
    fields = ["cw_published", "cw_url", "memo", "nico_published", "nico_url", "pages", "part_number", "title", "story"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "cw_published", "cw_url", "memo", "nico_published", "nico_url", "pages", "part_number", "title", "story",)
    list_display_links = ("cw_published", "cw_url", "memo", "nico_published", "nico_url", "pages", "part_number", "title", "story",)


@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    fields = ["cover_image", "memo", "released", "site", "tag_line", "title"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "cover_image", "memo", "released", "site", "tag_line", "title",)
    list_display_links = ("cover_image", "memo", "released", "site", "tag_line", "title",)


@admin.register(Type_master)
class Type_masterAdmin(admin.ModelAdmin):
    fields = ["key", "name", "value"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "key", "name", "value",)
    list_display_links = ("key", "name", "value",)


@admin.register(Fragment)
class FragmentAdmin(admin.ModelAdmin):
    fields = ["memo", "title", "url", "place", "type_master", "story", "web_comic"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "memo", "title", "url", "place", "type_master", "story", "web_comic",)
    list_display_links = ("memo", "title", "url", "place", "type_master", "story", "web_comic",)


@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):
    fields = ["key", "memo", "number", "type_master"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "key", "memo", "number", "type_master",)
    list_display_links = ("key", "memo", "number", "type_master",)


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    fields = ["camera_zoom_level", "subtitle", "title", "type_master", "journey", "place", "comic", "magazine"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "camera_zoom_level", "subtitle", "title", "type_master", "journey", "place", "comic", "magazine",)
    list_display_links = ("camera_zoom_level", "subtitle", "title", "type_master", "journey", "place", "comic", "magazine",)


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    fields = ["memo", "name", "type_master"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "memo", "name", "type_master",)
    list_display_links = ("memo", "name", "type_master",)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    fields = ["name", "type_master"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "name", "type_master",)
    list_display_links = ("name", "type_master",)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    fields = ["altitude", "latitude", "longitude", "memo", "name", "venue"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "altitude", "latitude", "longitude", "memo", "name", "venue",)
    list_display_links = ("altitude", "latitude", "longitude", "memo", "name", "venue",)


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    fields = ["datetime", "number", "place", "route"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "datetime", "number", "place", "route",)
    list_display_links = ("datetime", "number", "place", "route",)


@admin.register(Scene)
class SceneAdmin(admin.ModelAdmin):
    fields = ["memo", "page", "place", "story", "type_master"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "memo", "page", "place", "story", "type_master",)
    list_display_links = ("memo", "page", "place", "story", "type_master",)


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    fields = ["description", "name", "type_master"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "description", "name", "type_master",)
    list_display_links = ("description", "name", "type_master",)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    fields = ["height", "title", "url", "width", "step", "type_master", "person"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "height", "title", "url", "width", "step", "type_master", "person",)
    list_display_links = ("height", "title", "url", "width", "step", "type_master", "person",)


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    fields = ["description", "url", "person", "type_master", "step"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "description", "url", "person", "type_master", "step",)
    list_display_links = ("description", "url", "person", "type_master", "step",)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fields = ["memo", "name", "user", "type_master"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "memo", "name", "user", "type_master",)
    list_display_links = ("memo", "name", "user", "type_master",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ["date_joined", "email", "first_name", "last_name", "username"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "date_joined", "email", "first_name", "last_name", "username",)
    list_display_links = ("date_joined", "email", "first_name", "last_name", "username",)
