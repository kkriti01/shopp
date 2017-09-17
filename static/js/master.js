app.controller('master', function($scope, $http)
{
    $http.get('/api/category/').then(function(response)
    {
        $scope.category = response.data;
    });

      $http.get('/api/cart/').then(function(response)
            {
                console.log("product api");
                $scope.product = response.data;
                $scope.count = response.data.length;
            });

});