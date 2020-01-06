<template>
  <div class="home">
    <button @click="$router.push('/new')">Add Quote</button>
    <hr />
    <div class="container">
      <div class="quote" v-for="quote in quotes" :key="quote.id" :quote="quote">
        <p>
          <em>"{{quote.quote}}"</em>
          by {{quote.quote_by}}
        </p>

        <span class="added-by">added by {{quote.added_by}}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "home",
  data: () => ({
    quotes: []
  }),
  created() {
    fetch("http://localhost:8000")
      .then(res => res.json())
      .then(response => {
        this.quotes = response.quotes;
      })
      .catch(e => {
        console.error(e.message);
      });
  }
};
</script>


<style  scoped>
.home {
  width: 100%;
}

button {
  cursor: pointer;
  border: 1px solid steelblue;
  border-radius: 5px;
  background: white;
  color: steelblue;
  height: 2em;
}

button:hover {
  background: steelblue;
  color: white;
}

.container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}

.quote {
  width: 29%;
  padding: 0.5rem;
  margin: 1%;
  border-radius: 10px;
  border: 1px solid steelblue;
  color: black;
}

.quote span.by {
  text-decoration: underline;
}

.quote .added-by {
  color: rgba(0, 0, 0, 0.6);
  margin-top: 3em;
}
</style>