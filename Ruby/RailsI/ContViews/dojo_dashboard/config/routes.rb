Rails.application.routes.draw do
    root "dojos#index"
    resources :dojos do
        resources :students
    end
    # get "dojos/new" => "dojos#new"
    # post "dojos" => "dojos#create"
    # get "dojos/:id" => "dojos#show"
    # get "dojos/:id/edit" => "dojos#edit"
    # patch "dojos/:id" => "dojos#update"
    # delete "dojos/:id" => "dojos#destroy"
end
