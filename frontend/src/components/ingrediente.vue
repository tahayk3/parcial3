<template>
  <div>
    <table class="table table-striped mt-4">
      <thead>
      <tr>
        <th scope="col">ID</th>
        <th scope="col">Nombre</th>
        <th scope="col">Descripcion</th>
        <th scope="col">No. Personas</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="input in directory.edges" :key="input.id">
        <td>{{ input.node.id }}</td>
        <td>{{ input.node.name }}</td>
        <td>{{ input.node.descripcion }}</td>
        <td>{{ input.node.personas }}</td>
        <td><a :href="`/ingredientes/editar/${input.node.id}/${input.node.name}`">Editar</a></td>
      </tr>
      </tbody>
    </table>
    <td><a :href="`/ingredientes/ingresar/`">Crear</a></td>
  </div>

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

