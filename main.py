from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


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
        return AudioInterface()


if __name__ == '__main__':
    # run загружает kv файл с названием класса без суффикса App
    AudioApp().run()
