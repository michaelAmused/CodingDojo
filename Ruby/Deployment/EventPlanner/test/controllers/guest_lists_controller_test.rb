require 'test_helper'

class GuestListsControllerTest < ActionDispatch::IntegrationTest
  test "should get create" do
    get guest_lists_create_url
    assert_response :success
  end

  test "should get destroy" do
    get guest_lists_destroy_url
    assert_response :success
  end

end
