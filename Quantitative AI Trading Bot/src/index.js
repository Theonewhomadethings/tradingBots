body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

* {
  font-family: "ヒラギノ角ゴ Pro W3",
    "Hiragino Kaku Gothic Pro",
    Osaka,
    "メイリオ",
    Meiryo,
    "ＭＳ Ｐゴシック",
    "MS PGothic",
    sans-serif;

}

code {

  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;
}



/* div containing tables and metrics*/
#info {
  margin: 0 auto;
  margin-top: 50px;
  margin-bottom: 50px;

}


/* div containing the metrics */
#flex {
  width: 50%;
  margin: 0 auto;
  display: flex;
  flex-direction: row;
}

/* text for the metric title */
#metricName {
  font-size: 20px;
}

/* each metric (title and value)*/
#metric {
  margin-left: 20px;
  margin-right: 50px;
}

/* div for all frontend components in Analysis_Chart*/
#analysis {
  margin-bottom: 150px;
  margin-top: -50px;
}


/* css for the html tables */
.table {
  text-align: center;
  height: 300px;
  overflow-y: scroll;
  display: inline-block;
  margin-top: 50px;
  border: 1px solid black;
  width: 300px;
  margin-bottom: 50px;
  margin-left: 10px;
  margin-right: 10px;

}


/* input box css */
.formInput {
  margin-left: 5px;
  margin-right: 10px;
  margin-top: 50px;
  border-radius: 8px;
}

/* submit button css */
.button {
  padding: 5px 15px;
  background: rgb(255, 255, 255);
  border-radius: 8px;
}

/* select dropdown css*/
#selectMenu {
  height: 28px;
  width: 100px;
}

/* css for the text data stating the date ranges */
#ranges {
  margin-top: -100px;
  margin-left: 20px;
  float: left;
  text-align: left;
  position: absolute;

}

/* css for each list item inside the date ranges text */
#list_item {
  margin-top: 6px;
  font-size: 12px;
}

/* css for the div containing both tables */
#table_parent {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 700px;
}
