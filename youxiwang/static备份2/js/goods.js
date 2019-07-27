var vue = new Vue({
	el: '#app',
	data () {
	    return {
	      data: "",
	      cards: [],
	      has_prev: true,
	      has_next: true,
	      iter_pages: [],
	      prev_num: 1,
	      next_num: 1,
	    }
	},
	methods: {
		onClick: function(id){
			location.href = "detail.html?"+id;
		},
		add_card: function(id){
			$.get("/add_card/"+id, function (resp) {
				if (resp.errno == 0) {
					console.log(resp.errmsg);
				} else {
					console.log(resp.errmsg);
				}
			})
		},
	},

  	mounted () {
  		var url = window.location.search;
		p = url.replace("?","");
		if (p == "") {
			p = 1;
		}
		p = parseInt(p);

    	axios.get('/session')
		  .then((resp) => {
		  	this.data = resp.data.username;
		    console.log(resp);
		  })
		  .catch(function (error) {
		    console.log(error);
		  });

		$.get("/goods/"+p, function (resp) {
			vue.cards = resp.data;
			vue.has_prev = resp.has_prev;
			vue.has_next = resp.has_next;
			vue.iter_pages = resp.iter_pages;
			vue.prev_num = resp.prev_num;
			vue.next_num = resp.next_num;
			console.log(resp);
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