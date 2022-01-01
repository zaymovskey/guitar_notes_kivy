from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform

if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.RECORD_AUDIO])

kv = '''
#: import audio_player plyer.audio
<AudioInterface>:
    audio: audio_player
    orientation: 'vertical'

    Label:
        id: state
        text: 'Audio is: '+str(root.audio.state)

    Label:
        id: audio_location
        text: 'Audio is saved at - '+ str(root.audio.file_path)

    Button:
        id: record_button
        text: 'START RECORD'
        on_release: root.start_recording()

    Button:
        id: play_button
        text: 'PLAY'
        on_release: root.start_playing()
'''


class AudioInterface(BoxLayout):
    audio = ObjectProperty()
    has_recording = False

    def start_recording(self):
        state = self.audio.state
        if state == 'ready':
            self.audio.start()
        if state == 'recording':
            self.audio.stop()
            self.has_recording = True
        self.update_labels()

    def start_playing(self):
        state = self.audio.state
        if state == 'playing':
            self.audio.stop()
        else:
            self.audio.play()
        self.update_labels()

    def update_labels(self):
        record_button = self.ids['record_button']
        play_button = self.ids['play_button']
        state_label = self.ids['state']

        state = self.audio.state
        play_button.disabled = not self.has_recording

        state_label.text = 'AudioPlayer State: ' + state

        if state == 'ready':
            record_button.text = 'START RECORD'

        if state == 'recording':
            record_button.text = 'STOP RECORD'
            play_button.disabled = True

        if state == 'playing':
            play_button.text = 'STOP AUDIO'
            record_button.disabled = True
        else:
            play_button.text = 'PLAY AUDIO'
            record_button.disabled = False


class AudioApp(App):
    def build(self):
        Builder.load_string(kv)
        return AudioInterface()


if __name__ == '__main__':
    AudioApp().run()
