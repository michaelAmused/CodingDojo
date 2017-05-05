Rails.application.routes.draw do
  get 'likes/create'

  get 'likes/destroy'

  get 'secrets/index'

  resources :sessions, only: [:new, :create, :destroy]
  resources :users
  resources :secrets, only: [:index, :create, :destroy]
  resources :likes, only: [:create, :destroy]

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
