#!/usr/bin/env python3
"""Generate index.html for the Michael Jackson fan site."""
import json, html
from urllib.parse import quote

IMG = json.load(open("images.json"))

def ipath(slug, fallback=""):
    return IMG.get(slug, {}).get("path", fallback)

def icredit(slug):
    m = IMG.get(slug, {})
    if not m:
        return ""
    artist = html.escape(m.get("artist", "Unknown"))
    lic = html.escape(m.get("license", "See source"))
    title = m.get("title", "")
    page = "https://commons.wikimedia.org/wiki/" + quote(title.replace(" ", "_")) if title else "#"
    return f'Photo: {artist} \u00b7 <a href="{page}" target="_blank" rel="noopener">{lic}</a>'

# ---------------------------------------------------------------- timeline
TIMELINE = [
 dict(year="1958", title="A Star Is Born", img="jackson5-1971",
      text="Michael Joseph Jackson is born on August 29 in Gary, Indiana \u2014 the eighth of ten children "
           "in a working-class family. By age five he is already singing in front of anyone who will listen."),
 dict(year="1964", title="The Jackson 5", img="jackson5-1972",
      text="Michael joins brothers Jackie, Tito, Jermaine and Marlon in a family band that storms local "
           "talent shows across the Midwest. His voice \u2014 impossibly soulful for a child \u2014 makes him "
           "the obvious frontman."),
 dict(year="1969", title="Motown & \u201cI Want You Back\u201d", img="jackson5-1974",
      text="Signed to Motown, the Jackson 5's debut single rockets to No.\u00a01. An 11-year-old Michael "
           "is suddenly a national phenomenon."),
 dict(year="1972", title="Going Solo", img="jackson5-michael",
      text="While still with his brothers, Michael releases solo singles \u2014 \u201cGot to Be There\u201d "
           "and \u201cBen,\u201d the latter his first solo No.\u00a01 hit."),
 dict(year="1978", title="The Wiz", img="mj-1977",
      text="Michael stars as the Scarecrow in The Wiz and meets composer-producer Quincy Jones. The "
           "collaboration that follows will reshape popular music."),
 dict(year="1979", title="Off the Wall", img="mj-1981-quincy",
      text="With Quincy Jones producing, Off the Wall sells roughly 20 million copies and turns Michael "
           "into a solo superstar \u2014 and the first solo artist to land four Top-10 singles from one album."),
 dict(year="1982", title="Thriller", img="mj-1982",
      text="Released November 30, Thriller will become the best-selling album of all time, blending pop, "
           "rock, funk and disco behind \u201cBillie Jean,\u201d \u201cBeat It\u201d and the title track."),
 dict(year="1983", title="The Moonwalk", img="mj-1983",
      text="On the Motown 25 television special, Michael performs \u201cBillie Jean\u201d and debuts the "
           "moonwalk. It is instantly the most talked-about TV performance in pop history."),
 dict(year="1983", title="Thriller\u2019s Short Film", img="mj-1983-closeup",
      text="John Landis directs the 14-minute \u201cThriller\u201d film \u2014 a horror-movie spectacle that "
           "makes the music video an art form and sets a new bar for the medium."),
 dict(year="1984", title="Eight Grammys & the Pepsi Accident", img="mj-1984",
      text="Thriller wins a record-breaking eight Grammy Awards in a single night. Days earlier, pyrotechnics "
           "set his hair alight during a Pepsi commercial shoot \u2014 an accident that deepens his legend."),
 dict(year="1984", title="The Victory Tour", img="mj-1984-victory",
      text="Michael tours North America with his brothers one final time, playing to packed stadiums before "
           "an estimated two million fans."),
 dict(year="1985", title="\u201cWe Are the World\u201d", img="mj-1985-usa",
      text="Michael co-writes (with Lionel Richie) and performs on the USA for Africa charity anthem, "
           "assembling dozens of stars and raising millions for famine relief."),
 dict(year="1987", title="Bad", img="mj-1987-pepsi",
      text="The album Bad arrives with a Martin Scorsese-directed title video, and Michael launches his "
           "first-ever solo world tour."),
 dict(year="1988", title="The Bad World Tour", img="mj-1988",
      text="The Bad World Tour plays 123 shows to about 4.4 million people, including a record seven "
           "sold-out nights at Wembley Stadium. Michael also buys Neverland Ranch."),
 dict(year="1990", title="A White House Visit", img="mj-1990-bush",
      text="Michael is honoured at the White House as \u201cArtist of the Decade\u201d for his charitable "
           "work, a symbol of his extraordinary cultural reach."),
 dict(year="1991", title="Dangerous", img="mj-1992-live",
      text="Released November 26, Dangerous delivers \u201cBlack or White,\u201d \u201cRemember the Time\u201d "
           "and \u201cIn the Closet,\u201d and reasserts Michael as pop's most ambitious innovator."),
 dict(year="1992", title="The Dangerous World Tour", img="mj-1992-bucharest",
      text="The Dangerous World Tour opens, and his Bucharest concert is broadcast live to dozens of "
           "countries \u2014 one of the most-watched concerts ever televised."),
 dict(year="1993", title="Super Bowl XXVII", img="mj-1992-monza",
      text="Michael's halftime show at the Rose Bowl becomes one of the most-watched musical performances "
           "in American television history, ending with \u201cHeal the World.\u201d"),
 dict(year="1997", title="HIStory World Tour", img="mj-1997-lausanne",
      text="Following the 1995 HIStory album, the HIStory World Tour becomes the highest-attended concert "
           "tour by a solo artist, drawing around 4.5 million people."),
 dict(year="1999", title="MJ & Friends", img="mj-1999-slash",
      text="Michael headlines charity concerts in Seoul and Munich, joined on stage by guests including "
           "Slash, raising funds for children's causes around the world."),
 dict(year="2001", title="Invincible & 30 Years", img="mj-2003-cable",
      text="Invincible is released, and two star-studded concerts at Madison Square Garden celebrate 30 "
           "years of Michael Jackson as a solo artist."),
 dict(year="2005", title="Acquitted", img="mj-2003-vegas",
      text="After a 14-week trial that dominates headlines worldwide, Michael is acquitted of all charges "
           "and vows to focus again on music and his family."),
 dict(year="2009", title="This Is It", img="mj-2006-awards",
      text="Michael announces 50 sold-out shows at London's O2 Arena under the banner \u201cThis Is It.\u201d "
           "Rehearsals promise a spectacular return to the stage."),
 dict(year="2009", title="June 25", img="mj-2006-disney",
      text="On June 25, Michael Jackson dies at his Los Angeles home at the age of 50. Fans across the "
           "globe gather to mourn the loss of the King of Pop."),
 dict(year="2009", title="The Legacy", img="mj-walkoffame",
      text="A star on the Hollywood Walk of Fame, a farewell film (This Is It), and countless tributes "
           "follow \u2014 and his music keeps reaching new generations every year."),
]

# ---------------------------------------------------------------- concerts
CONCERTS = [
 dict(name="Motown 25", year="1983", venue="Pasadena Civic Auditorium, USA", img="mj-1983",
      text="The night the moonwalk was born. Michael's \u201cBillie Jean\u201d performance turned a TV "
           "anniversary special into the most famous few minutes in pop."),
 dict(name="Victory Tour", year="1984", venue="North America \u00b7 55 shows", img="mj-1984-jacksons",
      text="A final stadium run with the Jacksons, seen by roughly two million people and cementing "
           "Michael's drawing power as a live act."),
 dict(name="Bad World Tour", year="1987\u201389", venue="Worldwide \u00b7 123 shows", img="mj-1988",
      text="His first solo tour and, at the time, the biggest and highest-grossing concert tour ever "
           "undertaken by a solo artist."),
 dict(name="Dangerous World Tour", year="1992\u201393", venue="Worldwide \u00b7 69 shows", img="mj-1992-bucharest",
      text="A theatrical blockbuster. The Bucharest show was broadcast live worldwide and remains one "
           "of the most celebrated concert films of all time."),
 dict(name="Super Bowl XXVII Halftime", year="1993", venue="Rose Bowl, USA", img="mj-1992-monza",
      text="A jaw-dropping medley capped by \u201cHeal the World.\u201d The performance helped make the "
           "Super Bowl halftime show the cultural event it is today."),
 dict(name="HIStory World Tour", year="1996\u201397", venue="Worldwide \u00b7 82 shows", img="mj-1997-lausanne",
      text="The highest-attended tour of his career and by any solo artist, playing to around 4.5 million "
           "fans across five continents."),
 dict(name="MJ & Friends", year="1999", venue="Seoul & Munich", img="mj-1999-slash",
      text="Two enormous charity concerts for children's charities, with a guest list that included "
           "Slash and a host of international stars."),
 dict(name="30th Anniversary Special", year="2001", venue="Madison Square Garden, USA", img="mj-2003-cable",
      text="Two nights honouring three decades of solo artistry, with surprise appearances from friends "
           "and peers across the music world."),
 dict(name="This Is It", year="2009", venue="The O2 Arena, London \u00b7 50 shows", img="mj-2006-awards",
      text="A planned comeback residency that sold out 50 dates in minutes. Though it never happened, "
           "the rehearsals became the acclaimed film This Is It."),
]

# ---------------------------------------------------------------- songs (album -> popular songs with official YouTube IDs)
SONGS = [
 ("Off the Wall", "1979", [
   ("Don't Stop 'Til You Get Enough", "yURRmWtbTbo"),
   ("Rock with You", "5X-Mrc2l1d0"),
   ("Off the Wall", "MYPI0HZGVR4"),
   ("She's Out of My Life", "6DQJPL9Yuq0"),
 ]),
 ("Thriller", "1982", [
   ("Wanna Be Startin' Somethin'", "DsJlttdkybk"),
   ("The Girl Is Mine", "wHuRX5Or3ts"),
   ("Billie Jean", "Zi_XLOBDo_Y"),
   ("Beat It", "oRdxUFDoQe0"),
   ("Human Nature", "YNzuiRuQNYY"),
   ("P.Y.T. (Pretty Young Thing)", "V-l28QqV3jo"),
   ("Thriller", "sOnqjkJTMaA"),
 ]),
 ("Bad", "1987", [
   ("I Just Can't Stop Loving You", "PHZ1Bii7Uwk"),
   ("Bad", "Sd4SJVsTulc"),
   ("The Way You Make Me Feel", "HzZ_urpj4As"),
   ("Man in the Mirror", "PivWY9wn5ps"),
   ("Dirty Diana", "yUi_S6YWjZw"),
   ("Smooth Criminal", "h_D3VFfhvs4"),
 ]),
 ("Dangerous", "1991", [
   ("Black or White", "F2AitTPI5U0"),
   ("Remember the Time", "LeiFF0gvqcc"),
   ("In the Closet", "4qLY0vbrT8Q"),
   ("Jam", "JbHI1yI1Ndk"),
   ("Heal the World", "BWf-eARnf6U"),
 ]),
 ("HIStory", "1995", [
   ("Scream", "0P4A1K4lXDo"),
   ("You Are Not Alone", "pAyKJAtDNCw"),
   ("Earth Song", "XAi3VTSdTxU"),
   ("They Don't Care About Us", "t1pqi8vjTLY"),
   ("Stranger in Moscow", "pEEMi2j6lYE"),
 ]),
 ("Invincible", "2001", [
   ("You Rock My World", "1-7ABIM2qjU"),
   ("Butterflies", "QxnnAx9ED4M"),
   ("Cry", "mj3MfUR35CM"),
 ]),
]
SOLO_EARLY = [
 ("Got to Be There", "1972"), ("Ben", "1972"), ("Music & Me", "1973"),
 ("Forever, Michael", "1975"),
]

RECORDS = [
 ("~400M+", "Records sold worldwide"),
 ("70M+", "Copies of Thriller"),
 ("13", "Grammy Awards won"),
 ("8", "Grammys in a single night (1984)"),
 ("4.5M", "Fans on the HIStory World Tour"),
 ("#1", "Billboard Hot 100 hits"),
]

QUOTES = [
 "I'm never satisfied. I always want to do more.",
 "In a world filled with hate, we must still dare to hope.",
 "The greatest education in the world is watching the masters at work.",
 "Let us dream of tomorrow where we can truly love from the soul.",
 "If you enter this world knowing you are loved and you leave this world knowing the same, then everything that happens in between can be dealt with.",
]

# ---------------------------------------------------------------- builders
def fmt_tl():
    rows = []
    for i, e in enumerate(TIMELINE):
        side = "left" if i % 2 == 0 else "right"
        path = ipath(e["img"])
        img = (f'<div class="tl-img"><img src="{html.escape(path)}" alt="{html.escape(e["title"])}" '
               f'loading="lazy" /></div>') if path else ""
        rows.append(f"""
        <div class="tl-item {side}">
          <div class="tl-dot"></div>
          <div class="tl-card">
            {img}
            <div class="tl-body">
              <span class="tl-year">{e['year']}</span>
              <h3>{html.escape(e['title'])}</h3>
              <p>{html.escape(e['text'])}</p>
            </div>
          </div>
        </div>""")
    return "".join(rows)

def fmt_gallery():
    items = []
    order = ["jackson5-1971","jackson5-1972","jackson5-1974","jackson5-michael","mj-1977",
             "mj-1981-quincy","mj-1982","mj-1983","mj-1983-closeup","mj-1984","mj-1984-victory",
             "mj-1984-jacksons","mj-1985-usa","mj-1987-pepsi","mj-1988","mj-1988-in","mj-1988-himself",
             "mj-1990-bush","mj-1992-bucharest","mj-1992-monza","mj-1992-live","mj-1996-perth",
             "mj-1997-lausanne","mj-1997-stage","mj-1999-slash","mj-2003-cable","mj-2003-vegas",
             "mj-2006-awards","mj-2006-disney","mj-walkoffame"]
    caps = {
      "jackson5-1971":"The Jackson 5, early 1970s","jackson5-1972":"On tour with the Jackson 5, 1972",
      "jackson5-1974":"Michael, 1974","jackson5-michael":"Fronting the family band, 1976",
      "mj-1977":"The Jacksons, 1977","mj-1981-quincy":"With Quincy Jones, 1981",
      "mj-1982":"Thriller era, 1982","mj-1983":"Motown 25, 1983","mj-1983-closeup":"1983",
      "mj-1984":"The Grammy-winning year, 1984","mj-1984-victory":"Victory Tour, 1984",
      "mj-1984-jacksons":"With the Jacksons, 1984","mj-1985-usa":"We Are the World, 1985",
      "mj-1987-pepsi":"Bad era, 1987","mj-1988":"Bad World Tour, 1988","mj-1988-in":"1988",
      "mj-1988-himself":"1988","mj-1990-bush":"At the White House, 1990",
      "mj-1992-bucharest":"Dangerous Tour, Bucharest 1992","mj-1992-monza":"Live, 1992",
      "mj-1992-live":"Dangerous era, 1992","mj-1996-perth":"HIStory Tour, Perth 1996",
      "mj-1997-lausanne":"HIStory Tour, Lausanne 1997","mj-1997-stage":"HIStory Tour stage, 1997",
      "mj-1999-slash":"MJ & Friends, 1999","mj-2003-cable":"2003","mj-2003-vegas":"Las Vegas, 2003",
      "mj-2006-awards":"World Music Awards, 2006","mj-2006-disney":"With his children, 2006",
      "mj-walkoffame":"Star on the Hollywood Walk of Fame",
    }
    for slug in order:
        p = ipath(slug)
        if not p: continue
        items.append(f"""
        <figure class="g-item">
          <img src="{html.escape(p)}" alt="{html.escape(caps.get(slug,'Michael Jackson'))}" loading="lazy" />
          <figcaption>{html.escape(caps.get(slug,'Michael Jackson'))}</figcaption>
        </figure>""")
    return "".join(items)

def fmt_concerts():
    out = []
    for c in CONCERTS:
        p = ipath(c["img"])
        out.append(f"""
        <article class="concert">
          <div class="concert-img"><img src="{html.escape(p)}" alt="{html.escape(c['name'])}" loading="lazy" />
            <span class="concert-year">{c['year']}</span></div>
          <div class="concert-body">
            <h3>{html.escape(c['name'])}</h3>
            <div class="concert-venue">{html.escape(c['venue'])}</div>
            <p>{html.escape(c['text'])}</p>
          </div>
        </article>""")
    return "".join(out)

def fmt_albums():
    out = []
    for name, year, tracks in SONGS:
        rows = []
        for i, (title, vid) in enumerate(tracks, 1):
            rows.append(
                f'<li><button class="play" data-id="{vid}" aria-label="Play {html.escape(title)}">\u25b6</button>'
                f'<span class="tnum">{i}</span><span class="tname">{html.escape(title)}</span></li>')
        out.append(f"""
        <div class="album">
          <div class="album-head"><span class="album-year">{year}</span><h3>{html.escape(name)}</h3></div>
          <ul class="tracks">{''.join(rows)}</ul>
        </div>""")
    return "".join(out)

def fmt_records():
    return "".join(f'<div class="stat"><span class="stat-n">{html.escape(n)}</span>'
                   f'<span class="stat-l">{html.escape(l)}</span></div>' for n, l in RECORDS)

def fmt_quotes():
    return "".join(f'<blockquote>\u201c{html.escape(q)}\u201d</blockquote>' for q in QUOTES)

def fmt_credits():
    seen=set(); rows=[]
    for slug, m in IMG.items():
        if slug in seen or "path" not in m: continue
        seen.add(slug)
        title=m.get("title",""); 
        page="https://commons.wikimedia.org/wiki/"+quote(title.replace(" ","_")) if title else "#"
        rows.append(f'<li>{html.escape(m.get("artist","Unknown"))} \u2014 '
                    f'<a href="{page}" target="_blank" rel="noopener">{html.escape(m.get("license","See source"))}</a></li>')
    return "".join(rows)

HERO_IMG = ipath("mj-1992-bucharest")

SONGS_JS = """
<script>
(function(){
  var f=document.getElementById('ytPlayer'), ph=document.getElementById('playerPlaceholder'),
      now=document.getElementById('nowPlaying'), box=document.getElementById('playerBox');
  document.querySelectorAll('.play').forEach(function(b){
    b.addEventListener('click',function(){
      var li=b.closest('li'), name=li.querySelector('.tname').textContent, id=b.getAttribute('data-id');
      f.src='https://www.youtube.com/embed/'+id+'?autoplay=1&rel=0&modestbranding=1';
      if(ph) ph.classList.add('hide');
      if(now) now.textContent=name;
      document.querySelectorAll('.play').forEach(function(x){x.classList.remove('active');});
      b.classList.add('active');
      if(box && box.scrollIntoView && window.innerWidth<720) box.scrollIntoView({behavior:'smooth',block:'center'});
    });
  });
})();
</script>
"""

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Michael Jackson \u2014 The King of Pop | A Fan Tribute</title>
<meta name="description" content="A detailed fan tribute to Michael Jackson: his life story, career through the years, famous concerts and tours, records and legacy." />
<meta property="og:title" content="Michael Jackson — The King of Pop" />
<meta property="og:description" content="His life, his music, his concerts, his legacy — a fan tribute." />
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E%F0%9F%8E%A4%3C/text%3E%3C/svg%3E" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Dancing+Script:wght@600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
<style>
  :root {{
    --bg:#08080a; --panel:#131317; --panel2:#1a1a20; --line:#2a2a32;
    --text:#f4f4f7; --muted:#a2a2af; --red:#e00b2b; --gold:#ffd23f;
  }}
  *{{box-sizing:border-box}}
  html{{scroll-behavior:smooth; scroll-padding-top:70px}}
  body{{margin:0;background:var(--bg);color:var(--text);
    font-family:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
    line-height:1.6;-webkit-font-smoothing:antialiased}}
  img{{max-width:100%;display:block}}
  a{{color:inherit}}
  .wrap{{max-width:1180px;margin:0 auto;padding:0 clamp(1rem,4vw,2.5rem)}}
  .display{{font-family:"Bebas Neue",sans-serif;letter-spacing:0.02em;font-weight:400}}

  /* nav */
  nav.top{{position:sticky;top:0;z-index:50;background:rgba(8,8,10,.82);backdrop-filter:blur(12px);
    border-bottom:1px solid var(--line)}}
  nav.top .inner{{max-width:1180px;margin:0 auto;padding:.7rem clamp(1rem,4vw,2.5rem);
    display:flex;align-items:center;justify-content:space-between;gap:1rem}}
  nav.top .logo{{font-family:"Bebas Neue",sans-serif;font-size:1.35rem;letter-spacing:.06em}}
  nav.top .logo b{{color:var(--red)}}
  nav.top .links{{display:flex;gap:1.1rem;flex-wrap:wrap}}
  nav.top a{{color:var(--muted);text-decoration:none;font-size:.82rem;font-weight:600;letter-spacing:.03em}}
  nav.top a:hover{{color:var(--text)}}

  /* hero */
  .hero{{position:relative;min-height:82vh;display:flex;align-items:flex-end;overflow:hidden;
    border-bottom:1px solid var(--line)}}
  .hero .bg{{position:absolute;inset:0;background-image:url('{html.escape(HERO_IMG)}');
    background-size:cover;background-position:center 28%;filter:grayscale(.25) contrast(1.05)}}
  .hero .shade{{position:absolute;inset:0;background:
    linear-gradient(180deg,rgba(8,8,10,.55) 0%,rgba(8,8,10,.75) 55%,rgba(8,8,10,.97) 100%),
    radial-gradient(700px 500px at 80% 20%, rgba(224,11,43,.28), transparent 60%)}}
  .hero .content{{position:relative;z-index:2;padding:4rem 0 3rem;width:100%}}
  .hero .eyebrow{{font-size:.78rem;font-weight:700;letter-spacing:.35em;text-transform:uppercase;color:var(--gold)}}
  .hero h1{{font-family:"Bebas Neue",sans-serif;font-size:clamp(3.4rem,13vw,9rem);line-height:.9;
    margin:.3rem 0 .2rem;letter-spacing:.01em}}
  .hero h1 span{{color:var(--red)}}
  .hero .kicker{{font-family:"Dancing Script",cursive;font-size:clamp(1.6rem,4vw,2.6rem);color:#fff;opacity:.92}}
  .hero .dates{{margin-top:1rem;font-size:.95rem;letter-spacing:.18em;color:var(--muted)}}
  .hero .cta{{margin-top:1.6rem;display:flex;gap:.8rem;flex-wrap:wrap}}
  .btn{{display:inline-block;padding:.7rem 1.4rem;border-radius:999px;text-decoration:none;
    font-weight:700;font-size:.85rem;letter-spacing:.04em;border:1px solid var(--red);
    background:var(--red);color:#fff;transition:.2s}}
  .btn.ghost{{background:transparent;color:var(--text);border-color:#4a4a55}}
  .btn:hover{{transform:translateY(-2px)}}

  /* section */
  section{{padding:clamp(2.5rem,6vw,4.5rem) 0}}
  .sec-head{{margin-bottom:1.75rem}}
  .sec-head .tag{{font-size:.74rem;font-weight:700;letter-spacing:.3em;text-transform:uppercase;color:var(--red)}}
  .sec-head h2{{font-family:"Bebas Neue",sans-serif;font-size:clamp(2.2rem,6vw,3.6rem);margin:.15rem 0 0;line-height:1}}
  .sec-head p{{color:var(--muted);max-width:720px;margin:.6rem 0 0}}

  /* story */
  .story{{display:grid;grid-template-columns:1.4fr .9fr;gap:2.5rem;align-items:start}}
  .story p{{color:#d7d7de;font-size:1.02rem;margin:0 0 1rem}}
  .story .card-img{{border-radius:1rem;overflow:hidden;border:1px solid var(--line);position:sticky;top:80px}}
  .story .card-img img{{width:100%}}

  /* stats */
  .stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:1rem}}
  .stat{{background:linear-gradient(180deg,var(--panel),var(--panel2));border:1px solid var(--line);
    border-radius:.9rem;padding:1.2rem 1.1rem}}
  .stat-n{{font-family:"Bebas Neue",sans-serif;font-size:2.4rem;line-height:1;color:var(--gold);display:block}}
  .stat-l{{font-size:.78rem;color:var(--muted);letter-spacing:.03em}}

  /* timeline */
  .timeline{{position:relative;margin-top:1rem}}
  .timeline:before{{content:"";position:absolute;left:50%;top:0;bottom:0;width:2px;
    background:linear-gradient(var(--red),transparent);transform:translateX(-50%)}}
  .tl-item{{position:relative;width:50%;padding:0 2.2rem 2rem 0}}
  .tl-item.right{{margin-left:50%;padding:0 0 2rem 2.2rem}}
  .tl-dot{{position:absolute;top:.7rem;right:-9px;width:16px;height:16px;border-radius:50%;
    background:var(--red);box-shadow:0 0 0 4px rgba(224,11,43,.22)}}
  .tl-item.right .tl-dot{{right:auto;left:-9px}}
  .tl-card{{background:linear-gradient(180deg,var(--panel),var(--panel2));border:1px solid var(--line);
    border-radius:.9rem;overflow:hidden;transition:.25s}}
  .tl-card:hover{{border-color:rgba(224,11,43,.5);transform:translateY(-3px)}}
  .tl-img{{aspect-ratio:16/9;overflow:hidden;background:#0a0a0c}}
  .tl-img img{{width:100%;height:100%;object-fit:cover;object-position:center 25%}}
  .tl-body{{padding:1rem 1.1rem 1.15rem}}
  .tl-year{{font-family:"Bebas Neue",sans-serif;font-size:1.4rem;color:var(--gold);letter-spacing:.05em}}
  .tl-body h3{{margin:.1rem 0 .35rem;font-size:1.12rem}}
  .tl-body p{{margin:0;color:#c8c8d2;font-size:.9rem}}

  /* gallery */
  .gallery{{columns:3;column-gap:.9rem}}
  .g-item{{break-inside:avoid;margin:0 0 .9rem;position:relative;border-radius:.7rem;overflow:hidden;
    border:1px solid var(--line)}}
  .g-item img{{width:100%;transition:transform .5s}}
  .g-item:hover img{{transform:scale(1.06)}}
  .g-item figcaption{{position:absolute;left:0;right:0;bottom:0;padding:.9rem .7rem .55rem;
    font-size:.76rem;color:#fff;background:linear-gradient(transparent,rgba(8,8,10,.9))}}

  /* concerts */
  .concerts{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.25rem}}
  .concert{{background:linear-gradient(180deg,var(--panel),var(--panel2));border:1px solid var(--line);
    border-radius:.9rem;overflow:hidden;display:flex;flex-direction:column;transition:.25s}}
  .concert:hover{{transform:translateY(-4px);border-color:rgba(224,11,43,.5)}}
  .concert-img{{position:relative;aspect-ratio:16/10;overflow:hidden}}
  .concert-img img{{width:100%;height:100%;object-fit:cover;object-position:center 20%;transition:transform .5s}}
  .concert:hover .concert-img img{{transform:scale(1.06)}}
  .concert-year{{position:absolute;top:.7rem;left:.7rem;background:rgba(8,8,10,.7);border:1px solid rgba(255,255,255,.18);
    color:var(--gold);font-family:"Bebas Neue",sans-serif;font-size:1.05rem;padding:.1rem .55rem;border-radius:.4rem}}
  .concert-body{{padding:1rem 1.1rem 1.2rem}}
  .concert-body h3{{margin:0 0 .15rem;font-size:1.18rem}}
  .concert-venue{{font-size:.74rem;letter-spacing:.08em;text-transform:uppercase;color:var(--red);margin-bottom:.5rem}}
  .concert-body p{{margin:0;color:#c8c8d2;font-size:.9rem}}

  /* albums + song player */
  .player{{position:sticky;top:62px;z-index:30;display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);
    gap:1rem;background:linear-gradient(180deg,#1c1c24,#141419);border:1px solid var(--line);border-radius:1rem;
    padding:.9rem;margin-bottom:1.5rem;box-shadow:0 14px 34px rgba(0,0,0,.45)}}
  .player-frame{{position:relative;aspect-ratio:16/9;border-radius:.6rem;overflow:hidden;background:#000;border:1px solid var(--line)}}
  .player-frame iframe{{position:absolute;inset:0;width:100%;height:100%;border:0}}
  .player-placeholder{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;text-align:center;
    color:var(--muted);font-weight:700;padding:1rem;font-size:.95rem;
    background:radial-gradient(400px 200px at 50% 40%, rgba(224,11,43,.25), transparent 70%)}}
  .player-placeholder.hide{{display:none}}
  .player-info{{display:flex;flex-direction:column;justify-content:center;gap:.2rem}}
  .player-now{{font-size:.68rem;letter-spacing:.24em;text-transform:uppercase;color:var(--red);font-weight:700}}
  .player-name{{font-family:"Bebas Neue",sans-serif;font-size:clamp(1.3rem,3vw,1.9rem);line-height:1.05}}
  .player-note{{font-size:.72rem;color:var(--muted);margin-top:.35rem}}
  .albums{{display:grid;gap:1rem;grid-template-columns:repeat(auto-fill,minmax(330px,1fr))}}
  .album{{background:linear-gradient(180deg,var(--panel),var(--panel2));border:1px solid var(--line);
    border-left:3px solid var(--red);border-radius:.8rem;padding:1rem 1.1rem}}
  .album-head{{display:flex;align-items:baseline;gap:.6rem;margin-bottom:.55rem;border-bottom:1px solid var(--line);padding-bottom:.5rem}}
  .album-year{{font-family:"Bebas Neue",sans-serif;font-size:1.5rem;color:var(--gold)}}
  .album-head h3{{margin:0;font-size:1.15rem}}
  .tracks{{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:.25rem}}
  .tracks li{{display:flex;align-items:center;gap:.6rem;padding:.3rem .4rem;border-radius:.5rem;transition:background .15s}}
  .tracks li:hover{{background:rgba(255,255,255,.05)}}
  .tracks .play{{flex:none;width:30px;height:30px;border-radius:50%;border:0;background:var(--red);color:#fff;
    font-size:.72rem;line-height:1;cursor:pointer;display:grid;place-items:center;transition:transform .12s,background .15s}}
  .tracks .play:hover{{transform:scale(1.12)}}
  .tracks .play.active{{background:var(--gold);color:#111}}
  .tnum{{width:1rem;text-align:right;color:var(--muted);font-size:.76rem}}
  .tname{{flex:1;font-weight:600;font-size:.9rem}}
  .early{{margin-top:1rem;color:var(--muted);font-size:.85rem}}
  .early b{{color:var(--text)}}
  @media(max-width:720px){{.player{{grid-template-columns:1fr;position:static}}}}

  /* quotes */
  .quotes{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1rem}}
  blockquote{{margin:0;background:linear-gradient(180deg,var(--panel),var(--panel2));border:1px solid var(--line);
    border-radius:.9rem;padding:1.4rem 1.3rem;font-family:"Dancing Script",cursive;font-size:1.4rem;color:#eee}}
  blockquote:before{{content:"";display:block;width:34px;height:3px;background:var(--red);margin-bottom:.8rem}}

  /* credits */
  details.credits{{border-top:1px solid var(--line);margin-top:2rem;padding-top:1rem;color:var(--muted);font-size:.8rem}}
  details.credits summary{{cursor:pointer;color:var(--text);font-weight:600;margin-bottom:.6rem}}
  details.credits ul{{columns:2;column-gap:2rem;list-style:none;padding:0;margin:.4rem 0 0}}
  details.credits a{{color:#8f8f9c}}

  footer{{border-top:1px solid var(--line);padding:2rem 0;color:var(--muted);font-size:.8rem}}

  @media(max-width:820px){{
    .story{{grid-template-columns:1fr}} .story .card-img{{position:static}}
    .gallery{{columns:2}}
    .timeline:before{{left:9px}}
    .tl-item,.tl-item.right{{width:100%;margin-left:0;padding:0 0 1.6rem 2rem}}
    .tl-dot,.tl-item.right .tl-dot{{left:1px;right:auto}}
    details.credits ul{{columns:1}}
  }}
  @media(max-width:520px){{.gallery{{columns:1}}}}
</style>
</head>
<body>

<nav class="top"><div class="inner">
  <div class="logo"><b>MJ</b> \u00b7 KING OF POP</div>
  <div class="links">
    <a href="#story">Story</a><a href="#timeline">Timeline</a><a href="#years">Through the Years</a>
    <a href="#concerts">Concerts</a><a href="#albums">Albums</a><a href="#legacy">Legacy</a>
  </div>
</div></nav>

<header class="hero">
  <div class="bg"></div><div class="shade"></div>
  <div class="content wrap">
    <div class="eyebrow">A Fan Tribute</div>
    <h1>Michael <span>Jackson</span></h1>
    <div class="kicker">The King of Pop</div>
    <div class="dates">1958 \u00b7 GARY, INDIANA &nbsp;\u2014&nbsp; 2009 \u00b7 LOS ANGELES, CALIFORNIA</div>
    <div class="cta">
      <a class="btn" href="#story">Explore His Story</a>
      <a class="btn ghost" href="#concerts">Famous Concerts</a>
    </div>
  </div>
</header>

<!-- STORY -->
<section id="story"><div class="wrap">
  <div class="sec-head"><div class="tag">The Life</div><h2>A Once-in-a-Century Talent</h2></div>
  <div class="story">
    <div>
      <p>Michael Joseph Jackson was born on August 29, 1958, in Gary, Indiana \u2014 the eighth of ten
      children. From the moment he took the microphone as a small boy fronting his brothers, it was clear
      he was different: a singer with the timing of a seasoned professional and a performer who seemed to
      feel every note.</p>
      <p>As the lead voice of the Jackson 5 he became a child star, and as a solo artist he became a
      phenomenon. Working with producer Quincy Jones, he released a run of albums \u2014 <em>Off the Wall</em>,
      <em>Thriller</em> and <em>Bad</em> \u2014 that reshaped pop music and made the music video a serious
      art form. <em>Thriller</em> remains the best-selling album of all time.</p>
      <p>He was a dancer of extraordinary invention, refining steps like the moonwalk into global
      shorthand for genius. He was a perfectionist in the studio, a pioneer of spectacle on stage, and a
      philanthropist whose charity work touched children across the world. He was, and remains, the
      definitive pop icon \u2014 the benchmark against which everything since is measured.</p>
      <p>His death on June 25, 2009, at the age of 50, prompted an outpouring of grief unmatched in the
      history of popular culture. More than a decade later, his music is still streamed billions of times
      a year by fans old and new.</p>
    </div>
    <div class="card-img"><img src="{html.escape(ipath('mj-1988'))}" alt="Michael Jackson, 1988" /></div>
  </div>
</div></section>

<!-- STATS -->
<section style="padding-top:0"><div class="wrap">
  <div class="stats">{fmt_records()}</div>
</div></section>

<!-- TIMELINE -->
<section id="timeline"><div class="wrap">
  <div class="sec-head"><div class="tag">Over the Years</div><h2>His Life &amp; Career, Decade by Decade</h2>
    <p>From a six-year-old frontman in Gary, Indiana to the biggest star on the planet \u2014 the moments
    that built the legend.</p></div>
  <div class="timeline">{fmt_tl()}</div>
</div></section>

<!-- GALLERY -->
<section id="years"><div class="wrap">
  <div class="sec-head"><div class="tag">Gallery</div><h2>Through the Years</h2>
    <p>An evolution in pictures, from the Jackson 5 to the final rehearsals.</p></div>
  <div class="gallery">{fmt_gallery()}</div>
</div></section>

<!-- CONCERTS -->
<section id="concerts"><div class="wrap">
  <div class="sec-head"><div class="tag">Live</div><h2>Famous Concerts &amp; Tours</h2>
    <p>The performances that redefined what a concert could be \u2014 and the tours that broke attendance
    records around the world.</p></div>
  <div class="concerts">{fmt_concerts()}</div>
</div></section>

<!-- ALBUMS / SONGS -->
<section id="albums"><div class="wrap">
  <div class="sec-head"><div class="tag">Discography</div><h2>The Songs You Can Play</h2>
    <p>The most popular song from every album — press <b>\u25b6</b> to play the official video right here. 🎵</p></div>
  <div class="player" id="playerBox">
    <div class="player-frame">
      <iframe id="ytPlayer" title="Song player" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>
      <div class="player-placeholder" id="playerPlaceholder">🎵 Pick a song below and press ▶</div>
    </div>
    <div class="player-info">
      <div class="player-now">Now playing</div>
      <div class="player-name" id="nowPlaying">Nothing yet…</div>
      <div class="player-note">Plays the official video via YouTube. Songs © their respective owners.</div>
    </div>
  </div>
  <div class="albums">{fmt_albums()}</div>
  <p class="early"><b>Early solo albums:</b> {html.escape(' \u00b7 '.join(f"{n} ({y})" for n,y in SOLO_EARLY))}</p>
</div></section>

<!-- LEGACY -->
<section id="legacy"><div class="wrap">
  <div class="sec-head"><div class="tag">In His Words</div><h2>Quotes</h2></div>
  <div class="quotes">{fmt_quotes()}</div>

  <div class="sec-head" style="margin-top:3rem"><div class="tag">Forever</div><h2>The Legacy</h2></div>
  <div class="story">
    <div>
      <p>Michael Jackson changed the sound of pop, the look of the music video, and the scale of live
      performance. He made dances that the whole world learned, videos that played like cinema, and songs
      that still fill dance floors more than forty years after they were written.</p>
      <p>Since his passing, his influence has only grown. The concert film <em>This Is It</em> became one of
      the highest-grossing documentaries ever released; Cirque du Soleil built two hit shows around his
      catalogue; and the Broadway musical <em>MJ</em> brought his story to a new generation of theatregoers.
      Posthumous albums like <em>Michael</em> and <em>Xscape</em> topped charts worldwide.</p>
      <p>Inducted into the Rock &amp; Roll Hall of Fame and honoured with a star on the Hollywood Walk of
      Fame, he is remembered not only as the King of Pop, but as one of the most influential artists in the
      history of recorded music. The moonwalk, the glove, the fedora \u2014 they belong to him forever.</p>
    </div>
    <div class="card-img"><img src="{html.escape(ipath('mj-2006-awards'))}" alt="Michael Jackson, 2006" /></div>
  </div>
</div></section>

<div class="wrap">
  <details class="credits">
    <summary>Image credits &amp; licences (\u00a9 their respective authors, via Wikimedia Commons)</summary>
    <ul>{fmt_credits()}</ul>
  </details>
  <footer>
    A fan-made tribute for informational and educational purposes. Michael Jackson \u00b7 1958\u20132009.
    This site is not affiliated with the Jackson estate.
  </footer>
</div>

{SONGS_JS}
</body>
</html>
"""
open("index.html", "w").write(HTML)
print("wrote index.html", len(HTML), "bytes")
