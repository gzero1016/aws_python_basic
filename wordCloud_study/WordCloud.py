import wordcloud as wc

# 중복을 제거한 글들을 이미지로 만들어주는 것
text = "python 파이썬 test data user wordcloud"
wcText = wc.WordCloud(font_path="library/fonts/Arial Unicode.ttf",
                      background_color="white",
                      stopwords=["test", "data"],
                      min_font_size=10,
                      max_font_size=20,
                      width=1000,
                      height=1000)
wcText.generate_from_text(text)
# wcText.to_image().show()  # 보여주는거
wcText.to_file("test.png")  # 이미지 파일로 만들어주는것