<template>
  <div class="body">
    <div class="container">
      <div v-if="loading">Loading...</div>
      <div v-else>
        <h3>New Quote</h3>

        <form @submit.prevent="submitQuote">
          <div>
            <textarea placeholder="Quote text" rows="10" v-model="quote.quote" required />
          </div>

          <div>
            <input type="text" placeholder="Quote by" v-model="quote.quote_by" required />
          </div>

          <div>
            <input type="text" placeholder="Posted By" v-model="quote.added_by" required />
          </div>

          <div>
            <button type="submit">Save</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    loading: false,
    quote: {}
  }),
  methods: {
    submitQuote() {
      this.loading = false;

      fetch("http://localhost:8000", {
        method: "POST",
        headers: {
          "Content-type": "application/json"
        },
        body: JSON.stringify(this.quote)
      })
        .then(res => res.json())
        .then(response => {
          if (response) {
            alert("Quote added successfully");
            this.$router.push("/");
          } else {
            alert("Oops! We could not add your quote");
          }
        })
        .catch(e => {
          console.error(e.message);
        });
    }
  }
};
</script>
<style scoped >
.body {
  width: 100%;
}
h3 {
  font-weight: 300;
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
  width: 60%;
  margin: 15% 20% 20% 5%;
  border: 1px solid steelblue;
  padding: 2%;
}

form div {
  margin-top: 1em;
}

textarea,
input {
  width: 100%;
  font-size: 1em;
}
</style>