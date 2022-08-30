async function get_cupcakes() {
  res = await axios.get(`/api/cupcakes`);

  for (const ck of res.data.cupcakes) {
    $(".cupcake_holder").append(append_cupcake(ck));
  }
}

function append_cupcake(ck) {
  return `
    <div class="single-holder" data-cupcake-id=${ck.id}>
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

/*
==============================================
Upper Code Render The CupCakes to the Homepage
==============================================
*/

$(".add_new_cupcake").on("click", async function (e) {
  e.preventDefault();

  let flavor = $("#flavor").val();
  let size = $("#size").val();
  let rating = $("#rating").val();
  let image = $("#image").val();

  const new_cupcake = await axios.post(`/api/cupcakes`, {
    flavor,
    rating,
    size,
    image,
  });

  let new_add = append_cupcake(new_cupcake.data.cupcake);
  $(".cupcake_holder").append(new_add);
  alert("New cupcake added");
});

$(".cupcake_holder").on("click", ".delete-button", async function (e) {
  e.preventDefault();

  let id = $(e.target).parents(".single-holder").data("cupcake-id");

  $(e.target).parents(".single-holder").remove();

  await axios.delete(`/api/cupcakes/${id}`);

  alert("Cupcake is deleted");
});

$(".search_inp").on("keyup", async function (e) {
  let search = $(".search_inp").val();
  if ($(".search_inp").val() != "") {
    res = await axios.get(`/api/cupcakes/${search}`);
    $(".cupcake_holder").empty();
    for (const ck of res.data.cupcake) {
      $(".cupcake_holder").append(append_cupcake(ck));
    }
  } else {
    $(".cupcake_holder").empty();
    get_cupcakes();
  }
});

get_cupcakes();
