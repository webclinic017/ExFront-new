<template>
  <div style="text-align:center">
   <h1 id="eth">price:</h1><br>
   <h1 id="neth" hidden>price:</h1><br>
   <input id="per" class="form-control" type="number" step="any" name="">
   <h1 id="tp" class="alert alert-success">takeprofit:</h1><br>
   <h1 id="sl" class="alert alert-danger">stoploss:</h1><br>
   <button class="btn btn-success" onclick="submit()">submit</button>
  </div>
</template>

<!-- Page -->
<style src="@/vendor/styles/pages/authentication.scss" lang="scss"></style>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
document.addEventListener('DOMContentLoaded', ()=>{
  var data = {
      eth: document.getElementById('eth').innerHTML,
      neth:  document.querySelector('#neth').innerHTML,
      tp:  document.querySelector('#tp').innerHTML,
      sl:  document.querySelector('#sl').innerHTML,
      per:  document.querySelector('#per').value
    };
    function submit(){
      this.tp = this.eth + (this.eth * this.per)
    };
    async function getprice () {
      await axios
        .get('https://api1.binance.com/api/v3/ticker/bookTicker')
        .then(response => {
          data.eth = response.data[0].bidPrice
          if (response.data[0].bidPrice > this.neth) {
            data.neth = response.data[0].bidPrice
          }
          data.sl = data.neth - (data.neth * data.per)
          setTimeout(() => {
            location.reload()
          }, 5000)
        })
        .catch(() => {
        })
    }
    this.getprice()
})
    
</script>
