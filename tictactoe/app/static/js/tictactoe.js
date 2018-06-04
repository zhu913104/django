		$(document).ready(function() {

  $(".dots").click(function() {
    $(".guys, p").css("visibility", "hidden");
    $("td").css("visibility", "visible");
    aiCo = "#333";
    huCo = "white";
    console.log("white");
  });
  $(".dots2").click(function() {
    $(".guys, p").css("visibility", "hidden");
    $("td").css("visibility", "visible");
    console.log("black");
  });

  $("td").click(function() {
    move(this, huPlayer, huCo);
    console.log("clicked");

    $.ajax({
      type:'POST',
      url:"/result/",
      data:{
        'board':board.toString(),
        'legal':board.includes(" ")
      },
      error: function (xhr) {
            alert("Data");
        },
      success: function(Data){

        ai(Data);
      }

    })
  });
});
    var board = [" ", " ", " ", " ", " ", " ", " ", " ", " "];
    var huPlayer = "1";
    var aiPlayer = "2";
    var iter = 0;
    var round = 0;
    var aiCo = "white";
    var huCo = "#333";



function move(element, player, color,Data) {
  console.log("element"+ element.id);
  if (board[element.id] != "1" && board[element.id] != "2") {
    round++;
    $(element).css("background-color", color);
    board[element.id] = player;
    console.log(board);

    if (winning(board, player)) {
      setTimeout(function() {
        alert("YOU WIN");
        reset();
      }, 500);
      return;
    } else if (round > 8) {
      setTimeout(function() {
        alert("TIE");
        reset();
      }, 500);
      return;
    } 
  }
}
function ai(Data){
  {
      round++;
      var index = Data;
      var selector = "#" + index;
      $(selector).css("background-color", aiCo);
      board[index] = aiPlayer;
      console.log(board);
      console.log(index);
      if (winning(board, aiPlayer)) {
        setTimeout(function() {
          alert("YOU LOSE");
          reset();
        }, 500);
        return;
      } else if (round === 0) {
        setTimeout(function() {
          alert("tie");
          reset();
        }, 500);
        return;
      }
    }
}

function reset() {
  round = 0;
  board = [" ", " ", " ", " ", " ", " ", " ", " ", " "];
  $("td").css("background-color", "transparent");
}



// winning combinations
function winning(board, player) {
  if (
    (board[0] == player && board[1] == player && board[2] == player) ||
    (board[3] == player && board[4] == player && board[5] == player) ||
    (board[6] == player && board[7] == player && board[8] == player) ||
    (board[0] == player && board[3] == player && board[6] == player) ||
    (board[1] == player && board[4] == player && board[7] == player) ||
    (board[2] == player && board[5] == player && board[8] == player) ||
    (board[0] == player && board[4] == player && board[8] == player) ||
    (board[2] == player && board[4] == player && board[6] == player)
  ) {
    return true;
  } else {
    return false;
  }
}