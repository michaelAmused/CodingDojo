Rails.application.routes.draw do
  root 'users#index'
  post '/login/' => 'users#login'
  post '/register/' => 'users#register'
  get '/user/:id' => 'users#edit'
  patch '/user/:id' => 'users#update'
  get '/logout/' => 'users#logout'
  get '/events' => 'events#index'
  post '/events' => 'events#create'
  post '/events/guest_lists/:id' => 'guest_lists#create'
  get '/events/:id' => 'events#show'
  get '/events/:id/edit' => 'events#edit'
  patch '/events/:id' => 'events#update'
  delete '/events/:id' => 'events#destroy'
  
end
