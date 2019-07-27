// var vue = new Vue({
// 	el: '#app',
// 	data () {
// 	    return {
// 	      card_len: 0,	// 牌组长度
// 	      card_lis: [], // 牌组
// 	      fuse_len: 0, // 融合卡组长度
// 	      fuse_lis: [], // 融合卡
// 	    }
// 	},

// 	methods: {
// 		ck: function () {
// 			card = vue.card_lis.pop()
// 			vue.card_len = vue.card_lis.length;
// 			var html = "";
// 			if (card.card_type.indexOf("魔法") > -1 || card.card_type.indexOf("陷阱") > -1) {
// 				// 说明是魔法卡|陷阱卡
// 				html = '<a name="mofa" style="position:relative;">\
// 				<button class="zh" name="zh" style="position: absolute; top: -50px; left: 10px; width:50px;" hidden="hidden">召唤</button>\
// 				<button class="fz"  name="fz" style="position: absolute; top: -20px; left: 10px; width:50px;" hidden="hidden">放置</button>\
// 				<img style="height:80px" src="image/'+card.img+'">\
// 				</a>';
// 			} else {
// 				html = '<a name="guaishou" style="position:relative;">\
// 				<button class="zh" name="zh" style="position: absolute; top: -50px; left: 10px; width:50px;" hidden="hidden">召唤</button>\
// 				<button class="fz"  name="fz" style="position: absolute; top: -20px; left: 10px; width:50px;" hidden="hidden">放置</button>\
// 				<img style="height:80px" src="image/'+card.img+'" atk="'+card.atk+'" defend="'+card.defend+'">\
// 				</a>';
// 			}
			
// 			$(".my_hand").append(html);
// 		}
// 	},

// 	mounted () {
// 		$.get("/check_bag", function (resp) {
// 			console.log(resp);
// 			vue.card_len = resp.card.length;
// 			vue.card_lis = resp.card;
// 			vue.fuse_len = resp.fuse.length;
// 			vue.fuse_lis = resp.fuse;
// 			console.log(vue.card_lis)
// 		});
// 	}

// });
