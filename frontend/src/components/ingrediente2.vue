<template>

  <div>
    <form action="" @submit.prevent="mounted()">
      <div class="col-sm-6">
        <input v-model="name" name="" type="text" class="form-control">
        <input v-model="descripcion" descripcion="" type="text" class="form-control">
        <input v-model="personas" personas="" type="text" class="form-control">
        <button type="submit" name="button">Ingresar</button>
      </div>
    </form>
  </div>

</template>

<script>
  import axios from 'axios'
  export default{
    name: 'CompanyData',
    data(){
      return {
        name: '',
        descripcion: '',
        personas: '',
        directory: []
      }
    },
    methods: {
    async mounted () {
	try {
        var result = await axios({
          method: 'POST',
          url: 'http://localhost:8000/graphql',
          data: {
            query: `
            mutation{
  createCategory(input:{name:"`+this.name+`",descripcion:"`+this.descripcion+`",personas:"`+this.personas+`"}){
    category{
      id
      name
    }
  }
}
            `
          }
        })
        this.directory = result.data.data.allCategories
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>