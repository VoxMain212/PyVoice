from .profile import UserProfile, UserSettings, load_user_settings, get_profile_info


class AuthController:
    __instance = None

    def __new__(self):
        if self.__instance is None:
            self.__instance = super().__new__(self)
            self.__instance.__initialize()
        return self.__instance

    def __initialize(self):
        pass


class PyVoiceController:
    __instance = None

    self_user_profile: UserProfile
    user_settings: UserSettings

    audio_channels: list = []
    video_channels: list = []

    def __new__(self):
        if self.__instance is None:
            self.__instance = super().__new__(self)
            self.__instance.__initialize()
        return self.__instance
    
    def load_settings_and_profile(self, nickname=None, password=None):
        self.user_settings = load_user_settings(nickname)
        self.self_user_profile = get_profile_info(nickname, password)

    def __initialize(self):
        pass

    def handle(self, data):
        pass
