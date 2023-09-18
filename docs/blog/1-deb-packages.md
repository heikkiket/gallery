# Why you still need to create deb packages, not Flatpaks

Well, you don't, actually. You don't need to put clickbait titles to your blog posts either, but still some of us do.

I'm creating an UNIX-style image collection manager on my free time. I wrote about that in my previous post titled **[Why a world needs an UNIX-style image collection manager?](../why.md)**

Something I have had problems with is packaging. This is probably no surprise to anyone who has ever used Linux-based systems. I want people to be able to try my application if they want.

## Create a self-extracting binary?

So, I created a simple self-extracting binary from my gallery application, using a Python packaging tool called Shiv. Goodbye, packaging headaches! Just run this simple binary! It will then unpack itself to a hidden directory in your home directory. I told about it in social media and got a response that no one wants to download random binary and run it. (Besides, my friend didn't know how to put binary in `$PATH`.)

## Flatpaks and such to rescue?

But aren't there these new Flatpaks and Appimages you ask?

Yeah, but they aren't great for packaging command line applications. And when making UNIX-style application, of course it has command line interface as well, right?

Running applications with Flatpak is always done via flatpak command. Who wants to say something like `flatpak run org.myfineorg.gallery`? Not me! Appimages on the other hand have `.appimage` at the end of the filename. So `gallery.appimage`? I guess no one wants to run that kind of command either. And besides, you still have to know how to put appimage into `$PATH`.

## Revenge of Canonical

There's actually one modern package format that supports my use case. Guess what it is? Yesh, Snaps. I have heard so many times how horrible snap packages are and they are from Canonical you know so they are shit for sure... Anonymous commentors in Reddit  know these sorts of things.

To be fair, Snapcraft has a proprietary backend. That's a very legit reason not to use it.

And Snap is supported mainly on Ubuntu. What's the point using an "universal" package only supported on one system? I could create deb package instead, and it would work also on Debian and Mint (and whatever similar there is) maybe?

## Creating a deb package

That's what I tried to do. But deb packaging is a vast, swamp-like topic. Why can't there be a simple command that would take a tarball or something and turn that into a deb package?

Turns out there is. Of course it's totally unofficial and unmentioned in official deb packaging manuals. That tool is called [FPM](https://fpm.readthedocs.io/) which stands for *Effin Package Management*. I like the name.

## Packages, finally!

So here you go. [Install my gallery as a deb package](https://github.com/heikkiket/gallery/releases/tag/0.2.0) to your beloved Ubuntu box and test it. Come tell me how you liked it.

I wonder why modern package formats don't take command line into account. This is GNU/Linux after all, a system that is famous for its command line. And there's a ton of nice modern command line tools that I have to clone from Github or download random binaries from somewhere.

I also wonder why Debian packaging is so hard. Great mysteries of life.

