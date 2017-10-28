##Lab part I

1. Start by making a folder however you like, however you want to organize things. Make a file called `index.html` in your local folder (outside of Metis Git Repo to avoid git conflicts).

2. Here's how we'll start our own empty HTML pages from here on out:

  ```
  <!DOCTYPE html>
  <html>
  <head>
    <meta charset="utf-8">

    <style type="text/css">
      /*css to go here*/
    </style>
  </head>
  <body>

    <script src="https://d3js.org/d3.v4.min.js"></script>
    <script>
      //JS to go here
    </script>
  </body>
  </html>
  ```

2. Fire up a local server and open the page in the console. Test and see if your version loaded.  Make sure you are in the new local folder where you created the index.html.

```
# for Python 2
python -m SimpleHTTPServer 8000

# for Python 3
python -m http.server 8000
```

3. D3 is not intended just for data visualization; like jQuery, it's useful for DOM selection and manipulation, or simply for creating structured HTML pages. It's also public-facing on more web sites than you think. Let's explore some of its features on this [interactive article](http://www.nytimes.com/interactive/2015/05/03/upshot/the-best-and-worst-places-to-grow-up-how-your-area-compares.html?abt=0002&abg=1) income mobility.

4. Type and these in your browser console section and explore the results:

  ```
  d3.select('.g-custom-place')
  d3.selectAll('.g-custom-place')

  hint: use `style("color", <value>)`
  ```

5. Let's color all the custom places yellow to see how this thing works.

6. Open the newly created `index.html` in a text editor, and append an `h1` to the page via d3.select("body").append("h1").text("some text")

7. Let's also add some styles and a class to it.

8. More efficiently, D3 lets you "chain" your code. Handy!

9. Now do a data join. Make an array called parts and create a new `p` element for each.

  ```
    var parts = ["This is", "my first", "data join!"]

    var sentence = d3.select("body").selectAll("p")
        .data(parts)
      .enter()
        .append("p")
        .text(function(d) { return d; });
  ```

  That's a data join! Selecting elements you haven't created yet is a little strange, and we'll discuss it (and get plenty more experience in the next six weeks), but we won't linger for now. For more details, Scott Murray has [a great explanation](http://alignedleft.com/tutorials/d3/binding-data) and Mike Bostock Goes charactistically deep in [Thinking With Joins](http://bost.ocks.org/mike/join/).

10. As mundane as that was, that's the building block of every D3 chart you see on the internet.

##Lab part 2.
We're going to make the chart we drew by hand using D3.

1. Clear out or start a new `index.html`.

2. Make a Javascript object out of your tabular data in (quartet.tsv) and make sure you know how to manipulate it. (This is an annoying but useful exercise in getting useful in a text editor.) Choose One Group Data only (I, II, III or IV).  There are only 11 data rows per group, so this will build the muscle memory in writing Javascript Object arrays.  You only need X, Y attribute values in this data variable.

```
// Group I data
var data = [
{ x: 10, y: 8.04},
...
]

```

3. Let's first use pen and paper.  Take a Graph Paper and Plot the values (as scatter plot).  Compute Mean, Standard Deviation and write on the graph paper.

4. Now let's try to code this using D3 and produce the same Scatter plot. Add an SVG element of width 720 and height 400.

5. Using a data join, add a circle for every element of our array. Give it a radius 5 and a class, `anscombe-circle'. Inspect it in the browser. To start, I like to put a pink border around the SVG to make sure I knew it drew:

  ```
  /* Add CSS Styles in Header section of the html */
  svg {
    border: 1px solid #f0f;
  }
  ```

6. Position the circles based on their `x` and `y` attributes. How does SVG interpret these positions?

7. We need a [scale](https://github.com/mbostock/d3/wiki/Quantitative-Scales#linear-scales). Let's add one. (There's a trick.)

Checkpoint is [here](03-enter-append-scatter.html).

8. Let's label the coordinate positions of each using text. Is another data join really necessary?

9. Redo the original join, using groups first, then appending circles and text. Note SVG [transformation](http://www.w3.org/TR/SVG/coords.html) documentation, which is not that fun. Scott Murray [does better](http://chimera.labs.oreilly.com/books/1230000000345/ch08.html#_cleaning_it_up).

Checkpoint is [here](04-add-scales.html).

10. Maybe [axes](https://github.com/mbostock/d3/wiki/SVG-Axes) are in order? The built-in components are a little clunky, and [Gregor](https://twitter.com/driven_by_data) prefers not to use them at all, but you have to know the rules before you break them, so let's use them for now.

11. We might need to move our axes around. We'll go through the math. Also, it looks horrible unstyled. Let's inspect it and fix, using CSS.

12. The margins are a problem, and they will always be. Here's [a great trick](XXX) we'll use on every chart we make from here on out.

Checkpoint is [here](05-axes.html)

13. Let's style the chart. Things like [tickSize](https://github.com/mbostock/d3/wiki/SVG-Axes#tickSize) might help.

Checkpoint 4 is [here](06-styling-anscombe.html).

14. Using blockbuilder.org, let's make this a block.  Login with your github handle into blockbuilder.org.  Copy the style and JS portion.  Change the D3 version to d3.v3.min.js.

Congratulations for making this far!  You shared your Anscombe Public D3 Block.
