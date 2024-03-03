from django.http import JsonResponse
from django.shortcuts import render
from pytube import YouTube

# Create your views here.

def download_video(request):
    print(request.method, '=================== rtequst method \n\n')
    if request.method == 'POST':
        link = request.POST.get('video_link')
        print(link, '================== link \n\n')
        yt = YouTube(link)
        quality = yt.streams.filter(file_extension = 'mp4')
        highQuality = quality.get_highest_resolution()
        path_for_download = 'E:/youtube_project_folder'
        IsDownlaod = highQuality.download(output_path=path_for_download)
        print(IsDownlaod, '================ is Video Downlaod\n\n')
        if IsDownlaod:
            return JsonResponse({'msg':'success'})


    
    else:
        return render(request, 'index.html')

def demoAJAXSerialize(request):
    if request.method == 'POST':
        print(request.POST, '=================== REQUEST .OPST \n')

    else:
        return render(request, 'demo.html')