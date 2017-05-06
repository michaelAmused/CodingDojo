Rails.application.routes.draw do
  get 'guest_lists/create'

  get 'guest_lists/destroy'

  get 'comments/new'

  get 'comments/create'

  get 'comments/show'

  get 'comments/edit'

  get 'comments/update'

  get 'comments/destroy'

  get 'events/new'

  get 'events/create'

  get 'events/show'

  get 'events/edit'

  get 'events/update'

  get 'events/destroy'

  get 'users/index'

  get 'users/register'

  get 'users/login'

  get 'users/logout'

  get 'users/delete'

  get 'users/edit'

  get 'users/update'

  get 'users/show'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
