import ascii_magic
#image = "Komi_Shouko_holding_Introduction_to_Algorithms.jpg"
#image = "Dusttrust_fase1.png"
image = "Manaka_Ao_Holds_Introduction_to_Algorithms_v2.png"
ascii_art = ascii_magic.from_image(image)
ascii_art.to_html_file(
    "index.html",
    columns=420,
    width_ratio=2.5,
)
