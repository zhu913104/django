$(document).ready(function(){

$("#sub_update").click(function(){
  var commodity_id = $("#commodity_id").val()
  var commodity_name = $("#commodity_name").val();
  var commodity_num = $("#commodity_num").val();
  var commodity_date = $("#commodity_date").val();
  var commodity_dis = $("#commodity_dis").val();
  var commodity_img = $("#commodity_img").val();
  var commodity_price = $("#commodity_price").val();

  $.ajax({
      type: 'POST',      //傳送方式
      url: "/commodity/do_update/",  //傳送目的地
      data:{            //要傳送的資料 
        'commodity_id':commodity_id,
        'commodity_name':commodity_name,
        'commodity_num':commodity_num,
        'commodity_date':commodity_date, 
        'commodity_dis':commodity_dis, 
        'commodity_img':commodity_img, 
        'commodity_price':commodity_price, 

      },
      success: function (Data) {  /*假設後端執行"成功"後,做以下動作
(Data是回傳內容) */
        if(Data==200){
      window.location.href = "/commodity/";
        }
        else{
          alert("API 錯誤")
        }
    },
        error: function (e) {     /*假設後端執行"失敗"後,
做以下動作(e是錯誤訊息內容) */
        console.log(e);
      }
    });
  });
});
