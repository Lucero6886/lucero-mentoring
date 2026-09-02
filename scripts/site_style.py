# -*- coding: utf-8 -*-
"""Phong cách dùng chung cho mọi trang web sinh ra từ dự án.

Vì sao tách riêng: trang danh mục (docs/index.html) và trang hướng dẫn chọn đề tài
(docs/guide.html) phải trông như hai trang của cùng một hệ thống. Nếu mỗi script giữ
một bản CSS riêng thì sớm muộn hai trang sẽ lệch nhau — đúng loại trùng lặp mà dự án
này tránh ở mọi chỗ khác.

Dùng bởi: generate_site.py · generate_guide.py
"""

CSS = """
:root{
  --ground:#F7F8F6; --surface:#FFFFFF; --surface-2:#EEF1EE;
  --ink:#1C2733; --ink-2:#4A5763; --ink-3:#7A8791;
  --line:#D8DDD9; --line-soft:#E6EAE6;
  --accent:#0E7C6B; --accent-soft:#E2F0ED; --accent-ink:#0A5A4E;
  --warn:#8F6512; --warn-soft:#F6EEDA;
  --crit:#B3392E; --crit-soft:#F7E7E5;
  --low:#5B6770; --low-soft:#EAEDEF;
  --r:#6D4FA0; --r-soft:#EEE8F6;
  --mono:'IBM Plex Mono',ui-monospace,Menlo,Consolas,monospace;
  --display:'Archivo','Be Vietnam Pro',system-ui,sans-serif;
  --body:'Be Vietnam Pro',system-ui,-apple-system,'Segoe UI',sans-serif;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --ground:#12181D; --surface:#1A2229; --surface-2:#212B33;
    --ink:#E4EAE7; --ink-2:#A9B4B0; --ink-3:#7E8A87;
    --line:#33403F; --line-soft:#28332F;
    --accent:#4CC2AD; --accent-soft:#173B35; --accent-ink:#7FD8C8;
    --warn:#D9A94A; --warn-soft:#382E17;
    --crit:#E07A6F; --crit-soft:#3C2320;
    --low:#93A0A6; --low-soft:#26313A;
    --r:#A98BD6; --r-soft:#2A2138;
  }
}
:root[data-theme="dark"]{
  --ground:#12181D; --surface:#1A2229; --surface-2:#212B33;
  --ink:#E4EAE7; --ink-2:#A9B4B0; --ink-3:#7E8A87;
  --line:#33403F; --line-soft:#28332F;
  --accent:#4CC2AD; --accent-soft:#173B35; --accent-ink:#7FD8C8;
  --warn:#D9A94A; --warn-soft:#382E17;
  --crit:#E07A6F; --crit-soft:#3C2320;
  --low:#93A0A6; --low-soft:#26313A;
  --r:#A98BD6; --r-soft:#2A2138;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{background:var(--ground);color:var(--ink);font-family:var(--body);font-size:15.5px;line-height:1.6}
a{color:var(--accent-ink);text-underline-offset:3px}
a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible,summary:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:3px}
code{font-family:var(--mono);font-size:.88em;background:var(--surface-2);padding:.08em .35em;border-radius:4px}
.wrap{max-width:1040px;margin:0 auto;padding:0 20px}
/* nav */
.topnav{position:sticky;top:0;z-index:20;background:var(--ground);border-bottom:1px solid var(--line-soft)}
.topnav .wrap{display:flex;align-items:center;gap:18px;flex-wrap:wrap;padding-top:10px;padding-bottom:10px}
.topnav .logo{font-family:var(--display);font-weight:700;font-size:15px;letter-spacing:-.01em;margin-right:auto}
.topnav a{font-size:13.5px;color:var(--ink-2);text-decoration:none;padding:4px 2px}
.topnav a:hover{color:var(--accent-ink)}
/* hero */
.hero{padding:44px 0 26px}
.eyebrow{font-family:var(--mono);font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--accent-ink)}
h1{font-family:var(--display);font-weight:700;font-size:clamp(26px,4.6vw,38px);letter-spacing:-.015em;line-height:1.12;margin:10px 0 12px;text-wrap:balance}
.hero .meta{font-family:var(--mono);font-size:12.5px;color:var(--ink-3)}
.golden{background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:8px;padding:14px 18px;margin:20px 0 0;color:var(--ink-2)}
.golden b{color:var(--ink)}
section{padding:34px 0 6px;scroll-margin-top:64px}
h2{font-family:var(--display);font-weight:700;font-size:22px;letter-spacing:-.01em;border-bottom:2px solid var(--ink);padding-bottom:10px;margin-bottom:18px}
h3{font-family:var(--display);font-weight:600;font-size:16.5px;margin:24px 0 10px}
p{margin:0 0 12px}
.muted{color:var(--ink-2)}
/* tables */
.tw{overflow-x:auto;border:1px solid var(--line);border-radius:8px;background:var(--surface);margin:0 0 20px}
table{border-collapse:collapse;width:100%;font-size:13.5px}
th{font-family:var(--mono);font-size:11px;font-weight:500;letter-spacing:.07em;text-transform:uppercase;color:var(--ink-3);text-align:left;padding:9px 13px;border-bottom:1px solid var(--line);background:var(--surface-2)}
td{padding:9px 13px;border-bottom:1px solid var(--line-soft);vertical-align:top}
tr:last-child td{border-bottom:none}
td.date{font-family:var(--mono);font-size:12.5px;white-space:nowrap;font-variant-numeric:tabular-nums}
td.hard{color:var(--crit);font-weight:500}
/* pills */
.pill{display:inline-block;font-family:var(--mono);font-size:11px;font-weight:500;padding:2px 9px;border-radius:99px;white-space:nowrap}
.pill.P{background:var(--low-soft);color:var(--low)}
.pill.I{background:var(--accent-soft);color:var(--accent-ink)}
.pill.T{background:var(--warn-soft);color:var(--warn)}
.pill.R{background:var(--r-soft);color:var(--r)}
.pill.lv{background:var(--surface-2);color:var(--ink-2)}
.pill.alias{background:var(--accent-soft);color:var(--accent-ink)}
/* filter bar */
.filters{display:flex;flex-wrap:wrap;gap:10px;align-items:center;background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:12px 14px;margin-bottom:8px;position:sticky;top:46px;z-index:10}
.filters label{font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3)}
.filters select,.filters input[type=search]{font-family:var(--body);font-size:14px;color:var(--ink);background:var(--ground);border:1px solid var(--line);border-radius:6px;padding:7px 10px}
.filters input[type=search]{flex:1;min-width:180px}
.typechips{display:flex;gap:6px}
.typechips button{font-family:var(--mono);font-size:12px;padding:5px 12px;border-radius:99px;border:1px solid var(--line);background:var(--ground);color:var(--ink-2);cursor:pointer}
.typechips button[aria-pressed=true]{background:var(--ink);color:var(--ground);border-color:var(--ink)}
.count{font-family:var(--mono);font-size:12px;color:var(--ink-3);margin:6px 2px 14px}
/* topic cards */
.fam-head{font-family:var(--display);font-weight:700;font-size:15px;margin:22px 0 4px;color:var(--accent-ink)}
.fam-sub{font-size:13px;color:var(--ink-3);margin-bottom:10px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:10px;margin-bottom:10px;overflow:hidden}
.card summary{list-style:none;cursor:pointer;display:flex;flex-wrap:wrap;gap:8px 12px;align-items:baseline;padding:13px 16px}
.card summary::-webkit-details-marker{display:none}
.card summary:hover{background:var(--surface-2)}
.card .code{font-family:var(--mono);font-size:13px;font-weight:500;color:var(--accent-ink)}
.card .title{font-weight:600;flex:1 1 320px}
.card .title small{display:block;font-weight:400;font-size:12.5px;color:var(--ink-3);font-style:italic}
.card .body{padding:2px 16px 16px;border-top:1px solid var(--line-soft);font-size:14px}
.card .body dl{display:grid;grid-template-columns:130px 1fr;gap:7px 14px;margin-top:12px}
.card .body dt{font-family:var(--mono);font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:var(--ink-3);padding-top:2px}
.card .body dd{margin:0}
.mvt{background:var(--warn-soft);border-radius:6px;padding:2px 6px}
/* steps */
ol.steps{margin:0 0 14px 22px}
ol.steps li{margin-bottom:8px}
ul.plain{margin:0 0 14px 20px}
ul.plain li{margin-bottom:7px}
footer{margin-top:44px;border-top:1px solid var(--line);padding:18px 0 40px;font-size:12.5px;color:var(--ink-3)}
@media (max-width:640px){
  .card .body dl{grid-template-columns:1fr}
  .filters{position:static}
}
"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700'
         '&family=Be+Vietnam+Pro:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">')

# Địa chỉ kho công khai — dùng cho mọi link tuyệt đối trong trang sinh ra.
REPO = "https://github.com/Lucero6886/lucero-mentoring"
PAGES = "https://lucero6886.github.io/lucero-mentoring"

# Bổ sung riêng cho trang hướng dẫn chọn đề tài (docs/guide.html).
GUIDE_CSS = """
.stat-row{display:flex;flex-wrap:wrap;gap:14px;margin:18px 0 6px}
.stat{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:12px 18px;min-width:112px}
.stat b{display:block;font-family:var(--display);font-size:26px;line-height:1.1;color:var(--accent-ink)}
.stat span{font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3)}
.ladder{font-family:var(--mono);font-size:12.5px;line-height:2;background:var(--surface-2);
        border-left:3px solid var(--accent);padding:12px 16px;border-radius:0 8px 8px 0;overflow-x:auto}
.groupgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(258px,1fr));gap:12px;margin-top:14px}
.gcard{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:14px 16px;
       text-align:left;cursor:pointer;font:inherit;color:inherit;transition:border-color .12s,transform .12s}
.gcard:hover{border-color:var(--accent);transform:translateY(-1px)}
.gcard[aria-pressed="true"]{border-color:var(--accent);background:var(--accent-soft)}
.gcard .gid{font-family:var(--mono);font-size:12px;font-weight:500;color:var(--accent-ink)}
.gcard .gn{font-family:var(--display);font-weight:600;font-size:14.5px;margin:3px 0 6px;display:block}
.gcard .gd{font-size:13px;color:var(--ink-2);line-height:1.5}
.gcard .gm{font-family:var(--mono);font-size:11px;color:var(--ink-3);margin-top:8px;display:block}
.steps{counter-reset:s;list-style:none;margin-top:14px}
.steps li{counter-increment:s;position:relative;padding:0 0 16px 42px;border-left:2px solid var(--line-soft);margin-left:13px}
.steps li:last-child{border-left-color:transparent;padding-bottom:0}
.steps li::before{content:counter(s);position:absolute;left:-14px;top:-2px;width:26px;height:26px;border-radius:50%;
  background:var(--accent-soft);color:var(--accent-ink);font-family:var(--mono);font-size:12px;font-weight:500;
  display:grid;place-items:center;border:1px solid var(--accent)}
.steps li b{font-family:var(--display);font-size:15px;display:block;margin-bottom:2px}
.steps li p{font-size:13.5px;color:var(--ink-2)}
.gates{display:grid;gap:8px;margin-top:12px}
.gate{display:grid;grid-template-columns:52px 1fr;gap:12px;align-items:start;background:var(--surface);
      border:1px solid var(--line);border-radius:8px;padding:11px 14px}
.gate .gg{font-family:var(--mono);font-size:13px;font-weight:500;color:var(--accent-ink)}
.gate .gt{font-size:13.5px;color:var(--ink-2)}
.gate .gt b{color:var(--ink)}
.checklist{list-style:none;margin-top:10px}
.checklist li{padding:6px 0 6px 26px;position:relative;font-size:14px;border-bottom:1px solid var(--line-soft)}
.checklist li::before{content:"☐";position:absolute;left:0;top:5px;font-size:15px;color:var(--ink-3)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:22px}
@media(max-width:720px){.two{grid-template-columns:1fr}}
.rulebox{background:var(--crit-soft);border:1px solid var(--crit);border-radius:10px;padding:14px 18px;margin-top:14px}
.rulebox b{color:var(--crit)}
.okbox{background:var(--accent-soft);border:1px solid var(--accent);border-radius:10px;padding:14px 18px;margin-top:14px}
tr.hidden{display:none}
td.out{font-size:12.5px;color:var(--ink-2);max-width:340px}
"""
