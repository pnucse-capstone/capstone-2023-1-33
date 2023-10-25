import plotly.express as px

# 데이터
data = [
    {'wifi_download_speed': 11.79, 'wifi_upload_speed': 2.46, 'latitude': 35.231561, 'longitude': 129.082909},
    {'wifi_download_speed': 11.81, 'wifi_upload_speed': 2.7, 'latitude': 35.231588, 'longitude': 129.082927},
    {'wifi_download_speed': 8.03, 'wifi_upload_speed': 2.46, 'latitude': 35.231639, 'longitude': 129.082937},
    {'wifi_download_speed': 11.85, 'wifi_upload_speed': 2.59, 'latitude': 35.231687, 'longitude': 129.082949},
    {'wifi_download_speed': 25.86, 'wifi_upload_speed': 7.96, 'latitude': 35.231576, 'longitude': 129.082859},
    {'wifi_download_speed': 21.30, 'wifi_upload_speed': 5.64, 'latitude': 35.231607, 'longitude': 129.082872},
    {'wifi_download_speed': 25.38, 'wifi_upload_speed': 5.98, 'latitude': 35.231657, 'longitude': 129.082882},
    {'wifi_download_speed': 23.15, 'wifi_upload_speed': 4.18, 'latitude': 35.231711, 'longitude': 129.082887},
    {'wifi_download_speed': 24.93, 'wifi_upload_speed': 4.05, 'latitude': 35.231584, 'longitude': 129.082807},
    {'wifi_download_speed': 31.16, 'wifi_upload_speed': 10.51, 'latitude': 35.231630, 'longitude': 129.082819},
    {'wifi_download_speed': 34.53, 'wifi_upload_speed': 8.10, 'latitude': 35.231677, 'longitude': 129.082829},
    {'wifi_download_speed': 38.97, 'wifi_upload_speed': 11.06, 'latitude': 35.231725, 'longitude': 129.082835},
    {'wifi_download_speed': 32.27, 'wifi_upload_speed': 8.15, 'latitude': 35.231595, 'longitude': 129.082764},
    {'wifi_download_speed': 26.77, 'wifi_upload_speed': 10.42, 'latitude': 35.231646, 'longitude': 129.082776},
    {'wifi_download_speed': 32.51, 'wifi_upload_speed': 11.27, 'latitude': 35.231683, 'longitude': 129.082786},
    {'wifi_download_speed': 41.10, 'wifi_upload_speed': 13.71, 'latitude': 35.231728, 'longitude': 129.082795}
]

# 데이터프레임 생성
import pandas as pd
df = pd.DataFrame(data)

# 고정 크기 설정
marker_size = 15  # 원하는 마커 크기로 설정

# 'marker_size' 컬럼 추가
df['marker_size'] = marker_size

# 지도 시각화
fig = px.scatter_mapbox(
    df,
    lat='latitude',  # 위도 열
    lon='longitude',  # 경도 열
    size='marker_size',  # 'marker_size' 컬럼을 지정하여 고정 크기 설정
    color='wifi_download_speed',  # 마커 색상 설정
    hover_name='wifi_download_speed',  # 마커에 표시할 정보 설정
    zoom=18,  # 초기 줌 레벨
)

# 지도 스타일 설정 (Mapbox 스타일 사용)
fig.update_layout(mapbox_style="open-street-map")

# 그래프 출력
fig.show()



