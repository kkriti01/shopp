 app.controller('product', ['$scope', '$http','$routeParams', product]);

function product($scope, $http, $routeParams)
{
    console.log("this api", $routeParams.id)
    $http.get('/api/product/?category_id='+$routeParams.id).then(function(response)
    {
        console.log("product api");
        $scope.product = response.data;
    });

    $scope.add_cart = function (id) {
        console.log("item id is", id);
        $http({
        url: '/add_cart/',
        method: "POST",
            headers: {
        "Content-Type": "application/json"
    },
        data: { 'product_id' : id }
        })
        .then(function(response) {
            // success
            $http.get('/api/cart/').then(function(response)
            {
                console.log("product api");
                $scope.product = response.data;
                $scope.count = response.data.length;
            });
        },
        function(response) { // optional
            // failed
            console.log("failed");
        });

    }
};