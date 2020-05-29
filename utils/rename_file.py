from pathlib import Path


audio_paths = ['../audio', '../src/main/resources/base/audio']


def remove_1(path):
    """Remove ' 1' in filename for converted WAV files from iTunes."""
    for f in path.iterdir():
        if ' 1' in f.name:
            filename = f.name.replace(' 1', '')
            print(f'{f.name} -> {filename}')
            f.rename(path / filename)


if __name__ == '__main__':
    for path in audio_paths:
        remove_1(Path(path))
