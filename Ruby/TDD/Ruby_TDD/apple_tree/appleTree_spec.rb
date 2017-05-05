require_relative 'AppleTree'

RSpec.describe AppleTree do
  before do
    @a = AppleTree.new
  end
  it 'has age attribute with getter and setter methods' do
    @a.age = 0
    expect(@a.age).to eq(0)
  end
  it ' should have a height attribute with only a getter method' do
    expect(@a.height).to eq(1)
    expect{@a.height = 0}.to raise_error(NoMethodError)
  end

  it ' should have a count attribute with only a getter method' do
    expect(@a.count).to eq(0)
    expect{@a.count = 0}.to raise_error(NoMethodError)
  end

  it 'should have a method called year_gone_by' do
    # expect{@a.year_gone_by}.to raise_error(NoMethodError)
  end

  it 'add one year to the age attribute, 10% to height, and raise it\'s apple count to two' do
    @a.year_gone_by
    expect(@a.age).to eq(1)
    expect(@a.height).to eq(1.1)
    expect(@a.count).to eq(0)
  end

  it 'should not grow apples for the first three years of it\'s life' do
    1.upto(3)
    expect(@a.count).to eq(0)
  end

  it 'should have a method called pick_apples that takes all of the apples off the tree' do
    @a.year_gone_by.year_gone_by.year_gone_by.year_gone_by.year_gone_by
    @a.pick_apples
    expect(@a.count).to eq(0)
  end

  it 'should not grow apples if it\'s older than ten' do
    1.upto(11) { @a.year_gone_by }
    expect(@a.count).to eq(14)
  end

end
