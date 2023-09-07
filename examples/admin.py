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
    fields = ["cover_image_url", "isbn", "issued", "memo", "number", "obi", "released", "title"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "cover_image_url", "isbn", "issued", "memo", "number", "obi", "released", "title",)
    list_display_links = ("cover_image_url", "isbn", "issued", "memo", "number", "obi", "released", "title",)


@admin.register(Web_comic)
class Web_comicAdmin(admin.ModelAdmin):
    fields = ["cw_published", "cw_url", "memo", "nico_published", "nico_url", "pages", "part_number", "title"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "cw_published", "cw_url", "memo", "nico_published", "nico_url", "pages", "part_number", "title",)
    list_display_links = ("cw_published", "cw_url", "memo", "nico_published", "nico_url", "pages", "part_number", "title",)


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
    fields = ["memo", "title", "url"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "memo", "title", "url",)
    list_display_links = ("memo", "title", "url",)


@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):
    fields = ["key", "memo", "number"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "key", "memo", "number",)
    list_display_links = ("key", "memo", "number",)


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    fields = ["camera_zoom_level", "subtitle", "title"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "camera_zoom_level", "subtitle", "title",)
    list_display_links = ("camera_zoom_level", "subtitle", "title",)


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    fields = ["memo", "name"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "memo", "name",)
    list_display_links = ("memo", "name",)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    fields = ["name"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "name",)
    list_display_links = ("name",)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    fields = ["altitude", "latitude", "longitude", "memo", "name"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "altitude", "latitude", "longitude", "memo", "name",)
    list_display_links = ("altitude", "latitude", "longitude", "memo", "name",)


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    fields = ["datetime", "number"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "datetime", "number",)
    list_display_links = ("datetime", "number",)


@admin.register(Scene)
class SceneAdmin(admin.ModelAdmin):
    fields = ["memo", "page"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "memo", "page",)
    list_display_links = ("memo", "page",)


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    fields = ["description", "name"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "description", "name",)
    list_display_links = ("description", "name",)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    fields = ["height", "title", "url", "width"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "height", "title", "url", "width",)
    list_display_links = ("height", "title", "url", "width",)


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    fields = ["description", "url"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "description", "url",)
    list_display_links = ("description", "url",)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fields = ["memo", "name"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "memo", "name",)
    list_display_links = ("memo", "name",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ["date_joined", "email", "first_name", "last_name", "username"]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", "date_joined", "email", "first_name", "last_name", "username",)
    list_display_links = ("date_joined", "email", "first_name", "last_name", "username",)
