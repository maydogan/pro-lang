using System;
using System.IO; //dosya islemleri icin

namespace odev_1 {
	
	class FileIO {
		public static string Read(string file) {
		    string reader = "";
	        StreamReader read = new StreamReader(file);
	        reader = read.ReadToEnd();
		    read.Close();
			return reader;
		}
	}
	class Stack {
		private string[] items;
		private int indeks;

		public Stack(int n) {
		    items = new string[n];
		    indeks = -1;
		}
		
		public bool IsEmpty() {
		    return items[0] == null;
		}
		
		public int Push(string item) {
		    if (items[items.Length-1] == null) {
				items[++indeks] = item;
				return indeks;
		    } else
			    return -1;
		}
		
		public string Peek() {
			if (items[0] != null)
				return items[indeks];
			else
				return null;
		}
		
		public string Pop() {
			if (items[0] != null) {
				string i = items[indeks];
				items[indeks--] = null;
				return i;
			}
			else return null;
		}
	}
	
	class TagKontrol {
		private static string Again (string text ) {
			int i;
		 	string temp = "";
		 	for (i = 0; i < text.Length; i++)
				temp = temp + text[i] + text[i];
		 	return temp;
		}
		
		private static string Border (string text) {
			return String.Concat("[", text, "]");
		}
		
		private static string Upper (string text) {
			return text.ToUpper();
		}
		
		private static string Hide (string text) {
			return "";
		}
		
		private static bool balanced (string open, string  close) {
			string[] opens = {"<p>", "<u>", "<h>","<b>"};
			string[] closes = {"</p>", "</u>", "</h>","</b>"};
			return  Array.IndexOf(opens, open) == Array.IndexOf(closes, close);
		}
		
		private static string tag_proccess  (string tag, string str) {
			string[] tags = {"<b>", "<h>", "<u>", "<p>"};
			string[] app = {Again(str), Hide(str), Upper(str), Border(str)};
			return app [Array.IndexOf(tags, tag)];
		}
		
		public static string control (string s) {
			Stack tags = new Stack(200);
			Stack temp = new Stack(200);

			string text = "";
			string word = "";
			string tag  = "";
			bool state = false;
			int i;
			for (i = 0; i < s.Length; i++) {
				if (s[i] == '<') {
					state = true;
					if (word != "") {
						while ((tag = tags.Pop()) != null) {
							word = tag_proccess(tag, word);
							temp.Push(tag);
						}
						while ((tag = temp.Pop()) != null)
							tags.Push(tag);
						text += word;
					}
					word = "";
					tag += s[i];
				} else if (state == true  && s[i] == '>') {
					tag += s[i];
					if (tag[1] == '/') {
						if (tags.IsEmpty()) return "";
						if (balanced(tags.Peek(), tag))
							tags.Pop();
						else return "";
					} else tags.Push(tag);
					tag = "";
					state = false;
				} else if (state == true) tag += s[i];
				else word += s[i];
			}
			text += word;
			if (!tags.IsEmpty()) return "";
			return text;
		}
	}
	class MainForm {
		static void Main() {
			string s = FileIO.Read("C:/kaynak.txt");
			string text;
			if ((text = TagKontrol.control(s)) != "")
				Console.WriteLine("{0}", text);
			else
				Console.WriteLine("Kaynak dosyanin bicimleme etiketleri hatalidir, kontrol ediniz.");
		}
	}
}
