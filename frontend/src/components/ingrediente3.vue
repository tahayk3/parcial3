<template>

    <center>
    <div>
    <h1>Actualizar receta</h1>
    <br>
    <h2>ID: {{id=$route.params.id}} </h2>
    <form  action="" @submit.prevent="mounted()">
      <div class="col-sm-7">
         <div class="card-header">
        <h3>Nombre: {{$route.params.name}}</h3>
        <input v-model="name" name="" type="text" class="form-control">
        <h3>Descripcion: {{$route.params.descripcion}}</h3>
        <input v-model="descripcion" descripcion="" type="text" class="form-control">
        <h3>Ingredientes: {{$route.params.personas}}</h3>
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
        id: '',
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
  updateCategory(input:{id:"`+this.id+`", name:"`+this.name+`",descripcion:"`+this.descripcion+`",personas:"`+this.personas+`"}){
    category{
      id
      name
      descripcion
      personas
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