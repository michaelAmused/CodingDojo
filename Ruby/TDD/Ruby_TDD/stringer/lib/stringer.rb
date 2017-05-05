require "stringer/version"

module Stringer
  def self.spacify *strings
    strings.join(" ")
  end

  def self.minify text, len
    if len > text.length
      return text
    end
    "#{text[0...len]}..."
  end

  def self.replacify text, word, replace
    text = text.split(" ")

    text.map! do |elem|
      if elem == word
        replace
      else
        elem
      end
    end

    text.join(" ")
  end

  def self.tokenize text
    text.split(" ")
  end

  def self.removify text, word
    text = text.split(" ")
    text.reject! { |elem| elem == word }
    text.join(" ")
  end
end
