<template>

  <center>
    <div>
    <h1>Ingresar nueva receta</h1>
    <br>
    <form  action="" @submit.prevent="mounted()">
      <div class="col-sm-7">
         <div class="card-header">
        <h3>Nombre</h3>
        <input v-model="name" name="" type="text" class="form-control">
        <h3>Descripcion</h3>
        <input v-model="descripcion" descripcion="" type="text" class="form-control">
        <h3>Ingredientes</h3>
        <input v-model="personas" personas="" type="text" class="form-control">
        <br>
        <button type="submit" class="btn btn-warning" name="button">Ingresar</button>
        </div>
      </div>
    </form>
  </div>
  </center>

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