@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        image = request.files["image"]
        size = request.form["size"]
        with tempfile.NamedTemporaryFile() as temp1, tempfile.NamedTemporaryFile() as temp2:
            temp1.write(image.read())
            cmd = f"convert {temp1.name} -resize {size} {temp2.name}"
            os.system(cmd)
            temp2.seek(0)
            image = b64encode(temp2.read()).decode("utf-8")
            return render_template("index.html", image=image)

    return render_template("index.html")