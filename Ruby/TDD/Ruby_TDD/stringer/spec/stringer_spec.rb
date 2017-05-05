require "spec_helper"

RSpec.describe Stringer do
  it "concatenates undefined number of strings with a space" do
    expect(Stringer.spacify "Oscar", "Vazquez", "Zweig", "Olasaba", "Hernandez", "Ricardo", "Mendoza").to eq("Oscar Vazquez Zweig Olasaba Hernandez Ricardo Mendoza")
  end

  context "minifies the string depending on the argument value" do
    it "shortens the string up to the number of characters in the argument and adds '...'" do
      expect(Stringer.minify("Hello, I'm learning how to create a gem", 10)).to eq("Hello, I'm...");
    end

    it "returns the string if the argument is less than the length of the string" do
      expect(Stringer.minify("Hello", 10)).to eq("Hello")
    end
  end

  it "iterates over a string and replaces each instance a word with a replacement word" do
    expect(Stringer.replacify("I can't do this", "can't", "can")).to eq("I can do this")
  end

  it "iterates over a string and adds each word into an array" do
    expect(Stringer.tokenize("I love to code")).to eq(["I", "love", "to", "code"])
  end

  it "removes each instance of a word" do
    expect(Stringer.removify("I'm not a developer", "not")).to eq("I'm a developer")
  end
end
