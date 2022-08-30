async function get_cupcakes() {
  res = await axios.get(`/api/cupcakes`);

  for (const ck of res.data.cupcakes) {
    $(".cupcake_holder").append(append_cupcake(ck));
  }
}

function append_cupcake(ck) {
  return `
    <div data-cupcake-id=${ck.id}>
        <img src="${ck.image}" alt="(no image provided)">
        <div>
            <p class=cup_description> ${ck.flavor.toUpperCase()} ${
    ck.size.charAt(0).toUpperCase() + ck.size.slice(1)
  }  Rating: ${
    ck.rating
  }  <button class="delete-button btn btn-sm btn-danger">X</button> </p>
        </div>
    </div>`;
}

get_cupcakes();

/*
==============================================
Upper Code Render The CupCakes to the Homepage
==============================================
*/

$(".add_new_cupcake").on("click", function (e) {
    e.preventDefault();
    alert('Finish WOrk here Need too keep going')
});


