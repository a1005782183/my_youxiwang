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
	      search: "all",
	      s: ''
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
		search_func: function () {
			this.search = this.s;
			location.href = "/goods.html?1&"+this.s;
		}
	},

  	mounted () {
  		var url = window.location.search;
		p = url.replace("?","");
		p = p.split("&");
		if (p[0] == "") {
			p[0] = 1;
		}
		p[0] = parseInt(p[0]);
		if(p[1] == "")
			p[1] = "all"

    	axios.get('/session')
		  .then((resp) => {
		  	this.data = resp.data.username;
		    console.log(resp);
		  })
		  .catch(function (error) {
		    console.log(error);
		  });

		$.get("/goods/"+p[0]+"/"+p[1], function (resp) {
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