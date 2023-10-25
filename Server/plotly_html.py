import plotly.express as px
import plotly.io as pio

fig = px.imshow([[10.44, 9.81, 12.27, 14.15],
                [13.35, 11.24, 10.75, 11.14],
                [12.5, 12.94, 12.43, 11.52],
                [12.87, 13.35, 13.39, 12.02]])

fig2 = px.imshow([[19.62, 24.27, 27.31, 34.25],
                  [18.46, 28.40, 29.93, 27.61],
                  [23.15, 24.05, 19.64, 23.52],
                  [20.28, 6.57, 3.85, 6.81]])

# fig = px.scatter(x=range(10), y=range(10))
pio.write_html(fig, "/workspace/server/public/html/plotly_html2.html")
pio.write_html(fig2, "/workspace/server/public/html/plotly_html2.html")
