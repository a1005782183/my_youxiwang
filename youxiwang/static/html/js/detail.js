var vue = new Vue({
	el: '#app',
	data () {
	    return {
	      data: {},
	    }
	},
	methods: {
		
	},

  	mounted () {
  		var url = window.location.search;
		id = url.replace("?","");
		if (id == "") {
			id = 1;
		}
		id = parseInt(id);

		$.get("/detail/"+id, function (resp) {
			console.log(resp);
			vue.data = resp;
		});

		

		// axios.get('/cards_good')
		//   .then((response) => {
		//     console.log(response);
		//   })
		//   .catch(function (error) {
		//     console.log(error);
		//   });
	}

});