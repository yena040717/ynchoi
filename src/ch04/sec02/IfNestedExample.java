package ch04.sec02;

public class IfNestedExample {
	public static void main(String[] args) {		// TODO Auto-generated method stub
		int score=(int)(Math.random()*20)+81; //Math.random에 *20을 해줘서 0~19까지의 수를 랜덤으로 출력.
		System.out.println("점수: "+score);
		
		String grade;
		
		if(score>=90) {
			if(score>=95) {
				grade="A+";
			}else {
				grade ="A";
			}
		}else {
			if(score>=85) {
				grade="B+";
			}else {
				grade="B";
			}
		}
		
		System.out.println("학점: "+grade);
	}

}
