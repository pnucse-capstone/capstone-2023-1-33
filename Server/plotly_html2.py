# import plotly.graph_objects as go
import plotly.express as px

z1 = [[10.44, 9.81, 12.27, 14.15],
    [13.35, 11.24, 10.75, 11.14],
    [12.5, 12.94, 12.43, 11.52],
    [12.87, 13.35, 13.39, 12.02]]

z2 = [[19.62, 24.27, 27.31, 34.25],
      [18.46, 28.40, 29.93, 27.61],
      [23.15, 24.05, 19.64, 23.52],
      [20.28, 6.57, 3.85, 6.81]]

# heatmap1 = go.Figure(data=go.Heatmap(z=z1, colorscale='YlOrRd'))
# heatmap2 = go.Figure(data=go.Heatmap(z=z2, colorscale='YlOrRd'))
heatmap1 = px.imshow(z1, text_auto=True, color_continuous_scale='BuPu')
heatmap1.update_layout(title_text="download speed",
                       title_y=0.95,
                       title_x=0.5,
                       title_xanchor='center',
                       title_yanchor='middle',)
heatmap2 = px.imshow(z2, text_auto=True, color_continuous_scale='BuPu')
heatmap2.update_layout(title_text="upload speed",
                       title_y=0.95,
                       title_x=0.5,
                       title_xanchor='center',
                       title_yanchor='middle',)

heatmap1.write_html("/workspace/server/public/html/plotly_html1.html")
heatmap2.write_html("/workspace/server/public/html/plotly_html2.html")

#[32.48, 33.75, 52.50, 46.49],
#[43.88, 44.46, 43.72, 45.95],
#[42.85, 46.27, 31.55, 5.95],
#[14.043, 15.507, 7.613, 12.3325]
