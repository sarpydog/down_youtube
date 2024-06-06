import ssl
from pytube import YouTube
from progressbar import ProgressBar, Percentage, Bar, ETA

ssl._create_default_https_context = ssl._create_stdlib_context

def download_video(url):
    def progress_callback(stream, chunk, bytes_remaining):
        progress_bar.update(total_size - bytes_remaining)

    yt = YouTube(url, on_progress_callback=progress_callback)
    video = yt.streams.get_highest_resolution()

    total_size = video.filesize
    progress_bar = ProgressBar(
        maxval=total_size,
        widgets=["#1 Download video:",
                 Percentage(),
                 ' ',
                 Bar('=', '[', ']'),
                 ' ',
                 ETA()]
    ).start()

    print('Downloading...')
    video.download(filename='_video.mp4', output_path='.')
    progress_bar.finish()
    print('Download complete!')

if __name__ == '__main__':
    url = input('Please enter the YouTube video URL: ')
    print('Starting download...')
    download_video(url)
    print('Done!')

