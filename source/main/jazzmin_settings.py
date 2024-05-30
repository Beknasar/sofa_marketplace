JAZZMIN_SETTINGS = {
    # Название окна (по умолчанию будет использоваться current_admin_site.site_title, если отсутствует или None)
    "site_title": "Администрирование веб-магазина",

    # Заголовок на экране входа (максимум 19 символов) (по умолчанию будет использоваться current_admin_site.site_header, если отсутствует или None)
    "site_header": "Администрация веб-магазина",

    # Заголовок бренда (максимум 19 символов) (по умолчанию будет использоваться current_admin_site.site_header, если отсутствует или None)
    "site_brand": "Веб-магазин мебели",

    # Логотип для вашего сайта, должен быть доступен в статических файлах, используется для бренда в верхнем левом углу
    "site_logo": None,

    # Логотип для формы входа, должен быть доступен в статических файлах (по умолчанию используется site_logo)
    "login_logo": None,

    # Логотип для формы входа в темных темах (по умолчанию используется login_logo)
    "login_logo_dark": None,

    # CSS-классы, применяемые к логотипу выше
    "site_logo_classes": "img-circle",

    # Относительный путь к favicon для вашего сайта, будет использоваться по умолчанию site_logo, если отсутствует (идеально 32x32 пикселя)
    "site_icon": None,

    # Приветственный текст на экране входа
    "welcome_sign": "Добро пожаловать в магазин",

    # Авторское право в подвале
    "copyright": "OcOO 'Vector Bit'",

    # Список администраторов модели для поиска из строки поиска, строка поиска опущена, если исключена
    # Если вы хотите использовать одно поле поиска, вам не нужно использовать список, вы можете использовать простую строку
    "search_model": ["auth.User", "auth.Group"],

    # Имя поля в модели пользователя, которое содержит поле изображения/URL/Charfield или функцию обратного вызова, которая получает пользователя
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Ссылки для размещения в верхнем меню
    "topmenu_links": [

        # URL, который будет развернут (Разрешения могут быть добавлены)
        {"name": "Главная", "url": "admin:index", "permissions": ["auth.view_user"]},

        # Внешний URL, который открывается в новом окне (Разрешения могут быть добавлены)
        {"name": "Поддержка", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

        # модель администратора, на которую будет ссылка (Проверяются разрешения для модели)
        {"model": "auth.User"},

        # Приложение с выпадающим меню на все его страницы моделей (Проверяются разрешения для моделей)
        {"app": "books"},
    ],

    #############
    # User Menu #
    #############

    # Дополнительные ссылки для включения в меню пользователя в верхнем правом углу (тип url "app" не разрешен)
    "usermenu_links": [
        {"name": "Поддержка", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Side Menu #
    #############

    # Показывать ли боковое меню
    "show_sidebar": True,

    # Раскрыть ли меню автоматически
    "navigation_expanded": True,

    # Скрыть эти приложения при создании бокового меню, например (auth)
    "hide_apps": [],

    # Скрыть эти модели при создании бокового меню (например, auth.user)
    "hide_models": [],

    # Список приложений (и/или моделей) для определения порядка бокового меню (не обязательно включать все приложения/модели)
    "order_with_respect_to": [
        'moderator',
        'contacts', 'contacts.ArchiveContact',
        'information', 'information.VideoData', 'information.VideoLink', 'information.PhotoGallery',
        'faq'
    ],

    # Пользовательские ссылки для добавления в группы приложений, сгруппированные по имени приложения
    "custom_links": {
        "books": [{
            "name": "Создать сообщение",
            "url": "make_messages",
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },

    # Пользовательские значки для приложений/моделей бокового меню
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "information.VideoData": "fas fa-video",
        "information.VideoLink": "fab fa-youtube",
        "information.PhotoGallery": "fas fa-image",
        "information.KODEKS": "fas fa-code",
        "information.News": "fas fa-newspaper",
        "information.Organization": "fas fa-sitemap",
        "information.Management": "fas fa-user-tie",
        "information.Service": "fas fa-clipboard",
        "moderator.Moderator": "fab fa-black-tie",
        "faq.FAQ": "fas fa-comments",
        "faq.Question": "fas fa-question",
        "faq.Answer": "far fa-comment-dots",
        "contacts.ArchiveContact": "fas fa-address-book",
        "contacts.Anticore": "fas fa-address-card",
        "contacts.CollCenter": "fas fa-headset",
        "contacts.Contact": "fas fa-phone",
    },

    # Значки, которые используются, когда не указаны вручную
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Использовать модальные окна вместо всплывающих окон
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Относительные пути к пользовательским CSS/JS скриптам (должны присутствовать в статических файлах)
    "custom_css": None,
    "custom_js": None,
    # Указываете ли шрифт из fonts.googleapis.com (используйте custom_css для предоставления шрифта в противном случае)
    "use_google_fonts_cdn": True,
    # Показывать ли пользовательский интерфейс настройки в боковой панели
    "show_ui_builder": True,

    ###############
    # Change view #
    ###############
    # Отображать вид изменений как одна форма или вкладки, текущие варианты
    # - single
    # - horizontal_tabs (по умолчанию)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # переопределение форм изменений на основе модели администратора
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # Добавить выпадающий список языков в административную панель
    "language_chooser": False,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": True,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": True,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": True,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": True,
    "theme": "lumen",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": False
}
