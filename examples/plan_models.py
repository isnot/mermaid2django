from django.db import models


class Series(models.Model):
    """series"""

    """author 著者名 """
    author = models.CharField(
        verbose_name="著者名",
        max_length=255,
        blank=True,
    )
    """label レーベル コミック・シリーズのレーベル名称 例：電撃コミックスNEXT"""
    label = models.CharField(
        verbose_name="レーベル",
        max_length=255,
        blank=True,
    )
    """magazine_title 連載誌 雑誌連載の誌名か、Web連載のレーベル名称"""
    magazine_title = models.CharField(
        verbose_name="連載誌",
        max_length=255,
        blank=True,
    )
    """publisher 出版社 出版社 例：KADOKAWA"""
    publisher = models.CharField(
        verbose_name="出版社",
        max_length=255,
        blank=True,
    )
    """short_title 略称 略称や通称で代表的なもの"""
    short_title = models.CharField(
        verbose_name="略称",
        max_length=255,
        blank=True,
    )
    """title 作品名 正確な作品の名称"""
    title = models.CharField(
        verbose_name="作品名",
        max_length=255,
        blank=True,
    )


class Comic(models.Model):
    """comic 単行本 1巻、2巻、…。単巻のみの場合はseries_id=NULL"""

    """cover_image_url 書影url 版元ドットコムの書誌情報DBより"""
    cover_image_url = models.URLField(
        verbose_name="書影url",
        blank=True,
    )
    """isbn ISBN13 """
    isbn = models.CharField(
        verbose_name="ISBN13",
        max_length=255,
        blank=True,
    )
    """issued 発行日 巻末の奥付にある、初版発行日"""
    issued = models.DateField(
        verbose_name="発行日",
        auto_now_add=True,
    )
    """number  第n巻"""
    number = models.PositiveIntegerField(
        verbose_name="",
        blank=True,
    )
    """obi オビ 特徴的な帯の文言"""
    obi = models.CharField(
        verbose_name="オビ",
        max_length=255,
        blank=True,
    )
    """released 書店発売日 """
    released = models.DateField(
        verbose_name="書店発売日",
        auto_now_add=True,
    )
    """series_id  series comic one2many"""
    series_id = models.ForeignKey(
        "Series",
        verbose_name="",
        related_name="comic",
        on_delete=models.CASCADE,
    )
    """title 各巻タイトル 例：ざつ旅-That's Journey- 1"""
    title = models.CharField(
        verbose_name="各巻タイトル",
        max_length=255,
        blank=True,
    )


class Web_comic(models.Model):
    """web_comic Web連載 第1旅(1)、番外旅、一枚モノ、…"""

    """cw_published  """
    cw_published = models.DateField(
        verbose_name="",
        auto_now_add=True,
    )
    """cw_url Comic Walker """
    cw_url = models.URLField(
        verbose_name="Comic Walker",
        blank=True,
    )
    """magazine_id  magazine web_comic one2many"""
    magazine_id = models.ForeignKey(
        "Magazine",
        verbose_name="",
        related_name="web_comic",
        on_delete=models.CASCADE,
    )
    """memo  """
    memo = models.TextField(
        verbose_name="",
        blank=True,
    )
    """nico_published  """
    nico_published = models.DateField(
        verbose_name="",
        auto_now_add=True,
    )
    """nico_url ニコニコ静画 """
    nico_url = models.URLField(
        verbose_name="ニコニコ静画",
        blank=True,
    )
    """pages ページ数 """
    pages = models.PositiveIntegerField(
        verbose_name="ページ数",
        blank=True,
    )
    """story_id  story web_comic one2many"""
    story_id = models.ForeignKey(
        "Story",
        verbose_name="",
        related_name="web_comic",
        on_delete=models.CASCADE,
    )
    """title 各話の名前 """
    title = models.CharField(
        verbose_name="各話の名前",
        max_length=255,
        blank=True,
    )


class Magazine(models.Model):
    """magazine 雑誌連載 マオウ"""

    """memo  """
    memo = models.TextField(
        verbose_name="",
        blank=True,
    )
    """released 発売日 書店等での発売日 ※タイトルの月の2か月前27日前後"""
    released = models.DateField(
        verbose_name="発売日",
        auto_now_add=True,
    )
    """title タイトル 雑誌のタイトル 例：電撃マオウ 2020年1月号"""
    title = models.CharField(
        verbose_name="タイトル",
        max_length=255,
        blank=True,
    )


class Fragment(models.Model):
    """fragment その他媒体 表紙カラー、店舗特典、ポスター。コミック収録と未収録がある"""

    """character  character fragment many2many"""
    character = models.ManyToManyField(
        "Character",
        verbose_name="",
        related_name="fragment",
    )
    """memo  """
    memo = models.TextField(
        verbose_name="",
        blank=True,
    )
    """place_id  place fragment one2many"""
    place_id = models.ForeignKey(
        "Place",
        verbose_name="",
        related_name="fragment",
        on_delete=models.CASCADE,
    )
    """story_id  story fragment one2many"""
    story_id = models.ForeignKey(
        "Story",
        verbose_name="",
        related_name="fragment",
        on_delete=models.CASCADE,
    )
    """title  """
    title = models.CharField(
        verbose_name="",
        max_length=255,
        blank=True,
    )
    """url  """
    url = models.URLField(
        verbose_name="",
        blank=True,
    )
    """web_comic_id  web_comic fragment one2many"""
    web_comic_id = models.ForeignKey(
        "Web_comic",
        verbose_name="",
        related_name="fragment",
        on_delete=models.CASCADE,
    )


class Journey(models.Model):
    """journey 第〇旅、番外旅"""

    """key  """
    key = models.CharField(
        verbose_name="",
        max_length=255,
        blank=True,
    )
    """memo  """
    memo = models.TextField(
        verbose_name="",
        blank=True,
    )
    """type タイプ 1:本編 2:番外旅 9:その他"""
    type = models.PositiveIntegerField(
        verbose_name="タイプ",
        blank=True,
    )


class Story(models.Model):
    """story 単行本の単話 第〇旅前編、第〇旅後編。コミック未収録もある"""

    """camera_center_place_id  place story one2many このストーリーに登場する主な地点をすべて包含するような範囲（四角形）の中心"""
    camera_center_place_id = models.ForeignKey(
        "Place",
        verbose_name="",
        related_name="story",
        on_delete=models.CASCADE,
    )
    """camera_zoom_level  """
    camera_zoom_level = models.PositiveIntegerField(
        verbose_name="",
        blank=True,
    )
    """comic_id  comic story one2many"""
    comic_id = models.ForeignKey(
        "Comic",
        verbose_name="",
        related_name="story",
        on_delete=models.CASCADE,
    )
    """journey_id  journey story one2many"""
    journey_id = models.ForeignKey(
        "Journey",
        verbose_name="",
        related_name="story",
        on_delete=models.CASCADE,
    )
    """magazine_id  magazine story one2one"""
    magazine_id = models.OneToOneField(
        "Magazine",
        verbose_name="",
        related_name="story",
        on_delete=models.CASCADE,
    )
    """subtitle  """
    subtitle = models.CharField(
        verbose_name="",
        max_length=255,
        blank=True,
    )
    """title  """
    title = models.CharField(
        verbose_name="",
        max_length=255,
        blank=True,
    )


class Venue(models.Model):
    """venue 目的地 会津、松島、那須、…"""

    """comic_id  comic venue many2many"""
    comic_id = models.ManyToManyField(
        "Comic",
        verbose_name="",
        related_name="venue",
    )
    """journey_id  journey venue many2many"""
    journey_id = models.ManyToManyField(
        "Journey",
        verbose_name="",
        related_name="venue",
    )
    """name  """
    name = models.CharField(
        verbose_name="",
        max_length=255,
        blank=True,
    )
    """story_id  story venue many2many"""
    story_id = models.ManyToManyField(
        "Story",
        verbose_name="",
        related_name="venue",
    )


class Place(models.Model):
    """place 場所 東京駅の顔出しパネル、登場店舗、宿泊場所、観光名所、施設、交通拠点"""

    """altitude  """
    altitude = models.CharField(
        verbose_name="",
        max_length=255,
        blank=True,
    )
    """character_id  character place many2many"""
    character_id = models.ManyToManyField(
        "Character",
        verbose_name="",
        related_name="place",
    )
    """latitude  """
    latitude = models.CharField(
        verbose_name="",
        max_length=255,
        blank=True,
    )
    """longitude  """
    longitude = models.CharField(
        verbose_name="",
        max_length=255,
        blank=True,
    )
    """memo  """
    memo = models.TextField(
        verbose_name="",
        blank=True,
    )
    """name  """
    name = models.CharField(
        verbose_name="",
        max_length=255,
        blank=True,
    )
    """story_id  story place many2many"""
    story_id = models.ManyToManyField(
        "Story",
        verbose_name="",
        related_name="place",
    )
    """venue_id  venue place one2many"""
    venue_id = models.ForeignKey(
        "Venue",
        verbose_name="",
        related_name="place",
        on_delete=models.CASCADE,
    )


class Route(models.Model):
    """route 経路 placeを組み合わせて経路とする"""

    """memo  """
    memo = models.TextField(
        verbose_name="",
        blank=True,
    )
    """name  """
    name = models.CharField(
        verbose_name="",
        max_length=255,
        blank=True,
    )
    """place_id  place route many2many"""
    place_id = models.ManyToManyField(
        "Place",
        verbose_name="",
        related_name="route",
    )
    """story_id  story route many2many"""
    story_id = models.ManyToManyField(
        "Story",
        verbose_name="",
        related_name="route",
    )


class Character(models.Model):
    """character キャラクター 主要5人、編集部、他"""

    """description  """
    description = models.TextField(
        verbose_name="",
        blank=True,
    )
    """name  """
    name = models.CharField(
        verbose_name="",
        max_length=255,
        blank=True,
    )
    """story_id  story character many2many"""
    story_id = models.ManyToManyField(
        "Story",
        verbose_name="",
        related_name="character",
    )
    """type  """
    type = models.CharField(
        verbose_name="",
        max_length=255,
        blank=True,
    )


class Scene(models.Model):
    """scene シーン 名シーン、ざつ旅ARのマーカー"""

    """character_id  character scene many2many"""
    character_id = models.ManyToManyField(
        "Character",
        verbose_name="",
        related_name="scene",
    )
    """memo  """
    memo = models.TextField(
        verbose_name="",
        blank=True,
    )
    """place_id  place scene one2many"""
    place_id = models.ForeignKey(
        "Place",
        verbose_name="",
        related_name="scene",
        on_delete=models.CASCADE,
    )
    """story_id  story scene one2many"""
    story_id = models.ForeignKey(
        "Story",
        verbose_name="",
        related_name="scene",
        on_delete=models.CASCADE,
    )
    """venue_id  venue scene one2many"""
    venue_id = models.ForeignKey(
        "Venue",
        verbose_name="",
        related_name="scene",
        on_delete=models.CASCADE,
    )


class Photo(models.Model):
    """photo flickr (google place photo api有料)"""

    """height  """
    height = models.PositiveIntegerField(
        verbose_name="",
        blank=True,
    )
    """place_id  place photo one2many"""
    place_id = models.ForeignKey(
        "Place",
        verbose_name="",
        related_name="photo",
        on_delete=models.CASCADE,
    )
    """url  """
    url = models.URLField(
        verbose_name="",
        blank=True,
    )
    """user_id  user photo one2many"""
    user_id = models.ForeignKey(
        "User",
        verbose_name="",
        related_name="photo",
        on_delete=models.CASCADE,
    )
    """width  """
    width = models.PositiveIntegerField(
        verbose_name="",
        blank=True,
    )


class Tweet(models.Model):
    """tweet Twitter 石坂さん、鈴ヶ森さん、読者等、無関係"""

    """description  """
    description = models.TextField(
        verbose_name="",
        blank=True,
    )
    """place_id  place tweet one2many"""
    place_id = models.ForeignKey(
        "Place",
        verbose_name="",
        related_name="tweet",
        on_delete=models.CASCADE,
    )
    """type  """
    type = models.PositiveIntegerField(
        verbose_name="",
        blank=True,
    )
    """url  """
    url = models.URLField(
        verbose_name="",
        blank=True,
    )
    """user_id  user tweet one2many"""
    user_id = models.ForeignKey(
        "User",
        verbose_name="",
        related_name="tweet",
        on_delete=models.CASCADE,
    )


class User(models.Model):
    """user ユーザー 利用者"""

    """group_id  group user many2many"""
    group_id = models.ManyToManyField(
        "Group",
        verbose_name="",
        related_name="user",
    )
    """memo  """
    memo = models.TextField(
        verbose_name="",
        blank=True,
    )
    """name  """
    name = models.CharField(
        verbose_name="",
        max_length=255,
        blank=True,
    )
    """type  """
    type = models.PositiveIntegerField(
        verbose_name="",
        blank=True,
    )


class Group(models.Model):
    """group グループ"""

    """memo  """
    memo = models.TextField(
        verbose_name="",
        blank=True,
    )
    """name  """
    name = models.CharField(
        verbose_name="",
        max_length=255,
        blank=True,
    )
    """visibility  """
    visibility = models.PositiveIntegerField(
        verbose_name="",
        blank=True,
    )
