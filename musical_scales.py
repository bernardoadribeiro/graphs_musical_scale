class MusicalScales():
    """
        Musical Scale class to generate and load music scales.
        Parameters:
        - `type`: `['cromatic_ascending'|'cromatic_descending'|'diatonic']`
    """

    # Setup scales details
    # major_scale_tones = (0, 1., 2., 2.5, 3.5, 4.5, 5.5, 6.)
    # minor_scale_tones = (0, 1., 1.5, 2.5, 3.5, 4.5, 5., 6.)

    def __init__(self) -> None:

        self.major_scale_degree_tones = {
            # degree: tones,
            0: 0,    # Tonic
            1: 1.,   # 2nd degree
            2: 2.,   # 3rd
            3: 2.5,  # 4th
            4: 3.5,  # 5th
            5: 4.5,  # 6th
            6: 5.5,  # 7th
            # 7: 6.    # 8th - restart from begin
        }
        self.minor_scale_degree_tones = (0, 1., 1.5, 2.5, 3.5, 4.5, 5., 6.)

        self.cromatic_scale_ascending = [
            'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'B#']  # len: 12

        self.cromatic_scale_descending = [
            'C', 'Cb', 'D', 'Db', 'E', 'F', 'Fb', 'G', 'Gb', 'A', 'Ab', 'B', 'Bb']

    def _generate_cromatic_graph(self, type: str):
        cromatic_graph = {}
        if type == 'major':
            for note in self.cromatic_scale_ascending:
                # create a dict of dict for each note in ascending scale.
                cromatic_graph[note] = {}

        elif type == 'minor':
            for note in self.cromatic_scale_descending:
                # create a dict of dict for each note in ascending scale.
                cromatic_graph[note] = {}

        return cromatic_graph

    def generate_scale(self, tonic_note: str = 'C#', scale: str = 'major'):
        cromatic_scale = {}

        return cromatic_scale


class MajorCromaticScale():
    scale = {
        'C': {
            'C': 0.,  # Tonic
            'D': 1.,
            'E': 2.,
            'F': 2.5,
            'G': 3.5,
            'A': 4.5,
            'B': 5.5,
            # 'C': 6.  # Octave
        },
        'C#': {
            'C#': 0.,  # Tonic
            'D#': 1.,
            'E': 2.,
            'F': 2.5,
            'G': 3.5,
            'A': 4.5,
            'B': 5.5,
            # 'C': 6.,  # Octave
        },
        'D': {
            'C': 0.,  # Tonic
            'D': 1.,
            'E': 2.,
            'F': 2.5,
            'G': 3.5,
            'A': 4.5,
            'B': 5.5,
            'C': 6.,  # Octave
        },
        'D#': {
            'C': 0.,  # Tonic
            'D': 1.,
            'E': 2.,
            'F': 2.5,
            'G': 3.5,
            'A': 4.5,
            'B': 5.5,
            'C': 6.,  # Octave
        },
        'E': {
            'C': 0.,  # Tonic
            'D': 1.,
            'E': 2.,
            'F': 2.5,
            'G': 3.5,
            'A': 4.5,
            'B': 5.5,
            'C': 6.,  # Octave
        },
        'F': {
            'C': 0.,  # Tonic
            'D': 1.,
            'E': 2.,
            'F': 2.5,
            'G': 3.5,
            'A': 4.5,
            'B': 5.5,
            'C': 6.,  # Octave
        },
        'F#': {
            'C': 0.,  # Tonic
            'D': 1.,
            'E': 2.,
            'F': 2.5,
            'G': 3.5,
            'A': 4.5,
            'B': 5.5,
            'C': 6.,  # Octave
        },
        'G': {
            'C': 0.,  # Tonic
            'D': 1.,
            'E': 2.,
            'F': 2.5,
            'G': 3.5,
            'A': 4.5,
            'B': 5.5,
            'C': 6.,  # Octave
        },
        'G#': {
            'C': 0.,  # Tonic
            'D': 1.,
            'E': 2.,
            'F': 2.5,
            'G': 3.5,
            'A': 4.5,
            'B': 5.5,
            'C': 6.,  # Octave
        },
        'A': {
            'C': 0.,  # Tonic
            'D': 1.,
            'E': 2.,
            'F': 2.5,
            'G': 3.5,
            'A': 4.5,
            'B': 5.5,
            'C': 6.,  # Octave
        },
        'A#': {
            'C': 0.,  # Tonic
            'D': 1.,
            'E': 2.,
            'F': 2.5,
            'G': 3.5,
            'A': 4.5,
            'B': 5.5,
            'C': 6.,  # Octave
        },
        'B': {
            'C': 0.,  # Tonic
            'D': 1.,
            'E': 2.,
            'F': 2.5,
            'G': 3.5,
            'A': 4.5,
            'B': 5.5,
            'C': 6.,  # Octave
        },
        'B#': {
            'C': 0.,  # Tonic
            'D': 1.,
            'E': 2.,
            'F': 2.5,
            'G': 3.5,
            'A': 4.5,
            'B': 5.5,
            'C': 6.,  # Octave
        }
    }
