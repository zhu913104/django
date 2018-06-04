$(document).ready(function(){
$("#sub_delete").click(function(){
  var commodity_id = $("#commodity_id").val()
  $.ajax({
      type: 'POST',      //傳送方式
      url: "/commodity/do_delete/",  //傳送目的地
      data:{            //要傳送的資料 
        'commodity_id':commodity_id,
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
