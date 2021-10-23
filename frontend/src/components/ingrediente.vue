<template>
<center>
  <a :href="`/ingredientes/ingresar/`" class="btn btn-info">Crear</a>
  <div class="col-sm-7">
    <div class="card text-center" v-for="input in directory.edges" :key="input.id">
      <div class="card-header">
        <h1 class="card-title">{{ input.node.name }}</h1>
      </div>
      <div class="card-body">
        <h5>Descripcion</h5>
        <p class="card-text">{{ input.node.descripcion }}</p>
      </div>
      <div class="card-body">
        <h5>Ingredientes</h5>
        <p class="card-text">{{ input.node.personas }}</p>
      </div>
      <div class="card-footer text-muted">
        <td type="button" class="btn btn-warning"><a :href="`/ingredientes/editar/${input.node.id}/${input.node.name}/${input.node.descripcion}/${input.node.personas}`">Editar</a></td>
      </div>
      <br><br><br>
    </div>
  </div>
</center>

</template>

<script>
  import axios from 'axios'
  export default{
name: 'CompanyData',
    data(){
      return {
    directory: []
      }
    },
    async mounted () {
    try {
	var result = await axios({
		method: 'POST',
		url: 'http://localhost:8000/graphql',
		data: {
			query: `
			{
			    allCategories {
                    edges {
                    node {
                        id
                        name
                        descripcion
                        personas
                    }
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
</script>

